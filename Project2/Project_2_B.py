#import necessary classes to create an HTTP server and define behavior for incoming requests
from http.server import BaseHTTPRequestHandler, HTTPServer

#create a class implementing the baseHTTPRequestHandler class (to override to do_GET method for customization purposes)
class MyHTTPRequestHandler(BaseHTTPRequestHandler): 
    def do_GET(self): #overriding the do_GET method
        #let the client know the server has successfully processed the request
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html') #set content of response to html format
        self.end_headers()

        # Define HTML data as a page with my name as the title in big letters, an image of me from google, and some text describing the scenario underneath the picture
        html_content = '''
        <html>
        <head>
            <title>Simple HTTP Server</title>
        </head>
        <body>
            <h1>Konur Nordberg</h1> 
            <img src="https://www.staplessoccer.com/wp-content/uploads/2021/05/Track-Konur-Nordberg-1024x683.jpg">
            <p>What's up not really much to say here, just a picture of me jumping in high school.</p>
            <p>This is a demonstration of Project 2B - a simple http application - working. </p>
        </body>
        </html>
        '''
        self.wfile.write(html_content.encode()) #send HTML content as the response body to the client

def run():
    host = 'localhost'
    port = 8000 #used for testing purposes
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler) #instance of HTTPServer class using address and my modified RequestHandler class as arguments
    print(f'Starting server on {host}:{port}...') #display what is happening to the user specifically what host and what port are being used
    httpd.serve_forever() #always be listening for incoming requests until this code is terminated

run()
