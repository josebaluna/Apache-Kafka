#!/usr/bin/env python
from __future__ import print_function  # Print function in Python 2 and 3
from coapthon import defines
from coapthon.client.helperclient import HelperClient
from time import sleep
from functools import partial

import logging
import argparse
from kafka import KafkaProducer

# Global variables
observables = []    # list of observed paths.

# Observe callback receive function
def observe_callback(response, producer):
    producer.send('bigdataroom', str(response.payload).encode())  # Send the messageprint(response.payload)

def update_observable_resources(response):
    resources_list = response.payload.split(",")

    for resource in resources_list:
        elems = str(resource).split(";")

        if "obs" in elems: # if resource is observable
            # get path (position 0) and remove undesired characters
            observable_path = elems[0].translate(str.maketrans({'<': '', '>': ''}))

            # only append to global list if it has not been observed yet
            if observable_path not in observables:
                observables.append(observable_path)

def main(args):

    logging.disable(logging.DEBUG)  # Disable DEBUG logging

    while True:
        client = HelperClient(server=(args.host, args.port))
        response = client.discover()
        producer = KafkaProducer()

        # catching exception if the response doesn't contain a payload
        try:
            update_observable_resources(response)

            for path in observables:
                client.observe(path, partial(observe_callback, producer=producer))

        except AttributeError:
            print("Empty resource: Doesn't contain a payload")

        finally:
            sleep(20)    # 20 seconds between new discover


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-H', '--host',
        help="IP direction of the CoAP server, default: MULTICAST. ",
        default=defines.ALL_COAP_NODES
    )
    parser.add_argument(
        '-P', '--port',
        help="Port where CoAP server is listening, default: 5683",
        default=5683
    )

    main(parser.parse_args())
