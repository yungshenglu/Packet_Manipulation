#!/usr/bin/env python

from scapy.all import *

'''
Define your own protocol
'''
class Protocol(Packet):
    # Set the name of protocol (Task 2.)
    name = 'Student'

    # Define the fields in protocol (Task 2.)
    fields_desc = [
        StrField('dept', 'cs', fmt = 'H', remain = 0),
        IntEnumField('gender', 2, { 
            1: 'female',
            2: 'male' 
        }),
        StrField('id', '000000', fmt = 'H', remain = 0),
    ]

'''
Add customized protocol into IP layer
'''
bind_layers(TCP, Protocol, frag = 0, proto = 99)
conf.stats_classic_protocols += [Protocol]
conf.stats_dot11_protocols += [Protocol]