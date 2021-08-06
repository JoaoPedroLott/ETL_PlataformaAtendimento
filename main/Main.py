import time
import stomp
import ssl
import os
from Listener import ListenerMQ
from tests.Producer import sender
# from tests.Keys import hosts, password, username

hosts = [(os.environ['ENDPOINT_MQ_STOMP'], os.environ['PORT_MQ_STOMP'])]

listener = ListenerMQ()

conn = stomp.Connection(hosts, timeout=5, reconnect_attempts_max=5)
conn.set_listener('listener', listener)
conn.set_ssl(for_hosts=hosts, ssl_version=ssl.PROTOCOL_TLS)
conn.connect(os.environ['USERNAME_MQ'], os.environ['PASSWORD_MQ'], wait=True)
conn.subscribe('processo-elo', id='1')

sender(conn)

time.sleep(10)
conn.disconnect()
