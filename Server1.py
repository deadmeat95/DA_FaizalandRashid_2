import socket
import requests

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(1)
    print(f'Listening on port {SERVER_PORT} ...')

    while True:
        # Wait for client connections
        client, client_address = s.accept()
        print(f"{client_address} has coonnected!")

        # Get the client request
        with client as c:
            request = c.recv(1024).decode()
            print(request)

            # Send HTTP response
            response = """ \n
<!DOCTYPE html>
<html>
<body>

<h1>Faizal and Rashid first website</h1>

<p>Welcome to Singapore!</p>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHrNB1FljIFEDVp3YKTxpswXX3D2Yy2qkoEw&usqp=CAU" alt="Girl in a jacket" width="500" height="600">
</body>
</html>

"""
            #send response to client
            c.sendall("HTTP/1.1 200 OK".encode())
            c.sendall(response.encode())