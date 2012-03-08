menu.py
=======

This script allows you to easily generate a menu for presenting the user with several options. I've deliberatly kept it simple so that just about anybody can pick it up and understand what is going on. It's also my first python script so I've probably done everything wrong. However this works for me so I'm uploading what I've got and I'll come back and update it based on comments or patches I recieve.

Example Useage
--------------
	#!/usr/bin/python
	# Simple script that just does a DNS request on the selected site.
	import menu # Import the main script
	import socket # Allows us to do the DNS request
	import pprint # Allows for pretty printing of the DNS response
	
	message = "Which site would you like to retrieve DNS information for?"

	# Create the menu that we wish to present to the user
	servers = {
		'g': ['[G]oogle', 'google.com'],
		'f': ['[F]acebook', 'facebook.com'],
		'u': ['[U]buntu', 'ubuntu.com']
	}
	
	# Fetch the user's selection (there is an optional third parameter which specifies the number of chances given)
	selection = menu.getSelection(message, servers)
	
	# Do a DNS request on the selection and output it using the pretty print method
	pprint.pprint(socket.getaddrinfo(selection, 80))