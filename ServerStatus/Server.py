#!/usr/bin/python

class Server:
    """ Container for Server location and people to be notified."""
    location = ""
    notify_addresses = []
    def __init__(self, location, notify_addresses):
        self.location = location
        self.notify_addresses = notify_addresses
        
    def id( self ):
        return location