#!/usr/bin/python

class CurlTester:
    """Controls testing a server by using Curl to retrieve the specified URL."""
    _ssl_verify_host = 0
    _ssl_verify_peer = 0
    _ssl_ca = None

    def __init__( self, ssl_verify_host = 0, ssl_verify_peer = 0, ssl_ca = None):
        self._ssl_verify_host = ssl_verify_host
        self._ssl_verify_peer = ssl_verify_peer
        self._ssl_ca = ssl_ca
        
    
    def id( self ):
        return "CurlTester"
    
    def test( self, server ):
        return self._test_with_curl( server.location )
    
    def _curl_url( self, url ):
        import pycurl
        import cStringIO
        
        curled_value = ""
        curl = pycurl.Curl()
        buffer = cStringIO.StringIO()
        curl.setopt(curl.URL, url)
        
        if self._ssl_verify_host is not None:
            curl.setopt(curl.SSL_VERIFYHOST, self._ssl_verify_host)
        if self._ssl_verify_peer is not None:
            curl.setopt(pycurl.SSL_VERIFYPEER, self._ssl_verify_peer)
        if  self._ssl_ca not in (None, ""):
            curl.setopt(pycurl.CAINFO, self._ssl_ca)
        
        curl.setopt(curl.WRITEFUNCTION, buffer.write)
        
        try:
            curl.perform()
            curled_value = buffer.getvalue()
            buffer.close()
        
        except:
            pass
        
        return curled_value

    def _test_with_curl( self, url ):	
        curled_url = self._curl_url(url)
        if curled_url in (None, ""):
            return False
        return True