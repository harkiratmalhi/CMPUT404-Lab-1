#!/usr/bin/env python3
import socket
import time
import multiprocessing

#define address & buffer size
HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 1024

def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    return s

#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

#send data to server
def send_data(serversocket, payload):
    print("Sending payload")
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print ('Send failed')
        sys.exit()
    print("Payload sent successfully")

def data(s2, conn, payload):
    send_data(s2, payload)
    full_data = s2.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    print(full_data)
    s2.shutdown(socket.SHUT_WR)

def main():
    
    proxy_host = 'www.google.com'
    proxy_port = 80
    payload = f'GET / HTTP/1.0\r\nHost: {proxy_host}\r\n\r\n'
    buffer_size = 4096
    
    s = create_tcp_socket()
    
    remote_ip = get_remote_ip(proxy_host)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            s2 = create_tcp_socket()
            s2.connect((remote_ip, proxy_port))
            p = multiprocessing.Process(target=data,args=(s2, conn, payload))
            p.daemon = True
            p.start()
            conn.close()

if __name__ == "__main__":
    main()

