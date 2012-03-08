menu.py
=======

This script allows you to easily generate a menu for presenting the user with several options. I've deliberatly kept it simple so that just about anybody can pick it up and understand what is going on. It's also my first python script so I've probably done everything wrong. However this works for me so I'm uploading what I've got and I'll come back and update it based on comments or patches I recieve.

A quick example
---------------
	#!/usr/bin/python
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