import httplib

#Connect to IP Address at port
httpServ = httplib.HTTPConnection("10.62.0.213", 8000)
httpServ.connect()

httpServ.close()
