import httplib

#Connect to IP Address at port specidied bellow
httpServ = httplib.HTTPConnection("10.62.0.213", 8000)
httpServ.connect()

#Message to send to server
message = "hi"
httpServ.request('GET', "/echo.php?message=" + message)

response = httpServ.getresponse()
if response.status == httplib.OK:
    print "Response from server"
    print response.read()
	headers  = response.getheaders()
    for header in headers:
        print header

httpServ.close()
