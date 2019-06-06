#!/usr/bin/env python
from __future__ import print_function  # Print function in Python 2 and 3
from builtins import KeyboardInterrupt
from coapthon.server.coap import CoAP

import sys
import argparse

# import new resource defined in the file psutil resources
from classresources import BasicResource, ObservableResource, MemoryResource, CPUResource

def ignore_listen_exception(exception, server):
    type = exception.__class__.__name__
    print(type)
    return True

def main(args):
    # IP and Port configuration
    ip = "0.0.0.0"
    port = 5683
    # print which type of transmission is used:
    if args.unicast:
        print("Unicast")
    else:
        print("Multicast")

    # Create the CoAP server
    server = CoAP(
        (ip, port),
        multicast=not args.unicast,
        cb_ignore_listen_exception=ignore_listen_exception
    )

    # Register resources
    server.add_resource('info/', BasicResource(coap_server=server))
    server.add_resource('time/', ObservableResource(coap_server=server))
    server.add_resource('cpu/', CPUResource(coap_server=server))
    server.add_resource('memory/', MemoryResource(coap_server=server))

    try:
        # Start listening for incoming requests
        server.listen()

    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")
        sys.exit(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-U', '--unicast',
        help="If flag is used: UNICAST transmission. If not (default): MULTICAST transmission",
        default=False,
        action='store_true'
    )

    main(parser.parse_args())