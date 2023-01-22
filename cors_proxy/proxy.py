class proxy(server):
    def __init__(self, host, port):
        # `proxy` inherets from `server` so it must call the super constructor.
        super.__init__(self, host, port)

        # A URL pointing back to the proxy itself. This is used to funnle HTTP requests
        # through the proxy.

        self.pointer = 'http://{}:{}'.format(*self.address)

        # The last URL requested by a client is stored as a stack of strings. When a
        # client requests a relative path such as `./home`, the segment is pushed onto
        # the stack. In the special case of `../` paths, the previous segment is
        # popped of the stack. When a complete path is given, the stack is cleared and
        # set to that path.
        self.location = url()

    # Uses `get` to retrieve a web resource refered to by the given URL.

    def fetch(self, url):
        data = get(url)
        content = data.text

        return content

    # The core mechanism; replaces all existing URLs found in a page's source with
    # prefixed alters which point to the proxy. Hence all requests made by client
    # browsers, are funnled through the proxy.

    def proxify(self, content):
        proxyurl = '{}/http'.format(self.pointer)

        # This replaces all occurances of http(s) with a pointer back to the proxy.

        proxified = page.replace('http', proxyurl)

        return proxified

    # Finds a URL (if present) in a client HTTP request. When a client browser requests
    # a page through the proxy, this function returns the URL of the desired page. If
    # a URL is not found, it will return `False`.

    def findurl(self, request):
        # A regular expression pattern which identifies URLs within the request line.

        pattern = 'GET /(http.+)/ HTTP/\d\.\d'
        results = findall(pattern, request)

        if (results):
           # If the search returns results, select the and return the URL.

            url = results[0]

            return url

        return False

    # This function takes a proxified page (where all URLs point back to the proxy),
    # and encapsulates it into a HTTP response.

    def encapsulate(self, proxified):
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        footer = '\r\n\r\n\r\n'

        # Place the proxified content within the HTTP header and footer, forming a
        # complete packet.

        packet = header + proxified + footer

        return packet

    # handles a client request.

    def handle(self, client, info):
        # recieve a HTTP request from the client.

        request = self.recieve(client, 2048)

        # Find the URL (if present) in the request line.

        url = self.findurl(request)

        if (url):
            # Update the working

            self.location.changeto(url)

            # Fetch the contents of the resource at `url`.

            content = self.fetch(url)

            # Create the proxified version of the page source, then finally encapsulate
            # send it back to the client as a HTTP response.

            proxified = self.proxify(content)
            response = self.encapsulate(proxified)

            self.send(client, response)

        # Close the client connection.
