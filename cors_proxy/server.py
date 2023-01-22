class server(object):
    def __init__(self, host, port):
        self.socket = socket()
        self.address = (host, port)

    # Functions for sending and recieving data from connected client sockets.

    def send(self, client, data):
        packet = data.encode()
        client._send(packet)

    def recieve(self, client, length):
        packet = client.recv(length)
        data = packet.decode()

        return data

    # handles a client connection. This should be overiden by inheriting classes.

    def handle(self, client, info):
        pass

    # Listens for, and accepts client connections. When a client connects, it will
    # hand over control to the `handle` function as a thread.

    def listen(self):
        self.socket.bind(self.address)

        while (True):
            self.socket.listen(5)

            (client, info) = self.socket.accept()

            # Start `handle` as a new thread.

            start_new_thread(
                self._handle, (client, info)
            )

    # Closes a client socket's connection.

    def end(self, client):
        client.close()

    # Stops the server.

    def stop(self):
        self.socket.close()
