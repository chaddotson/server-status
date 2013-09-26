#!/usr/bin/python

class SimpleEmailNotifier:
    """Sends email to users."""
    _smtp_server = ""
    _smtp_port = None
    _from_address = ""
    
    def __init__( self, from_address, smtp_server, smtp_port=None ):
        self._smtp_server = smtp_server
        self._smtp_port = smtp_port
        self._from_address = from_address
        
    def _make_email_message(self, to_addresses, subject, message):
        from email.mime.text import MIMEText
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = self._from_address
        msg['To'] = ', '.join(to_addresses)
        return msg
    
    def _send_mail( self, smtp_connection, message ):
        import types
        if isinstance(message['To'], types.ListType):
            smtp_connection.sendmail(message['From'], message['To'], message.as_string())
        else:
            smtp_connection.sendmail(message['From'], [message['To']], message.as_string())
    
    def notify( self, to_addresses, subject, message, **kwargs ):
        import smtplib
        smtp_connection = None
        
        if self._smtp_port is not None:
            smtp_connection = smtplib.SMTP(self._smtp_server, self._smtp_port)
        else:
            smtp_connection = smtplib.SMTP(self._smtp_server)
    
        self._send_mail( smtp_connection, self._make_email_message( to_addresses, subject, message ) )
        
        smtp_connection.quit()