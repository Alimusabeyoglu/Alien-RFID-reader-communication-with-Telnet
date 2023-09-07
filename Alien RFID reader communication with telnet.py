import telnetlib

HOST = "192.168.1.100"
PORT = "23"

username = "alien" 
password = "password"

tn = telnetlib.Telnet(HOST, PORT) # Connection

print(tn.read_until(b"Username>").decode()) # Wait till prompted for username
tn.write(username.encode() + b'\n')

print(tn.read_until(b"Password>").decode()) # Wait till prompted for password
tn.write(password.encode() + b'\n')

while True:
    tn.write(input().encode() + b"\n") # Enter commands
    print(tn.read_until(b"Alien>").decode()) # Wait till prompted for new command line