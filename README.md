menu.py
=======

A quick example
---------------
`#!/usr/bin/python
import menu
import socket
import pprint

servers = {
	'g': ['[G]oogle', 'google.com'],
	'f': ['[F]acebook', 'facebook.com'],
	'u': ['[U]buntu', 'ubuntu.com']
}

message = "Which site would you like to retrieve DNS information for?"
selection = menu.getSelection(message, servers)
pprint.pprint(socket.getaddrinfo(selection, 80))
`

