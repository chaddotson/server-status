#!/usr/bin/python

class ServerTester:
    """Controls executing the tests and notifying users."""
    _notifiers = None
    _testers = None
    _notify_if_ok = False
    
    def __init__(self, tester, notifiers, notify_if_ok = False):
        self._notifiers = notifiers
        self._tester = tester
        self._notify_if_ok = notify_if_ok
    
    def _send_notifications( self, **kwargs ):
        for notifier in self._notifiers:
            notifier.notify( **kwargs )
    
    def test( self, servers ):
        for server in servers:
            if not self._tester.test( server ):
                self._send_notifications(to_addresses=server.notify_addresses, subject="Site Down!: " + server.location, message="Site Down!: " + server.location )
            elif self._notify_if_ok:
                self._send_notifications(to_addresses=server.notify_addresses, subject="Site Up!: " + server.location, message="Site Up!: " + server.location )                
                