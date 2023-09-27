filePath = "chatText/tts"
import socket
import config
count = 0
sock = socket.socket()
sock.connect((config.server, config.port))
sock.send(f"PASS {config.token}\n".encode('utf-8'))
sock.send(f"NICK {config.nickname}\n".encode('utf-8'))
sock.send(f"JOIN {config.channel}\n".encode('utf-8'))
while True:
    resp = sock.recv(2048).decode('utf-8')
    resp = resp.split(':')[-1]
    resp = resp.lower()
    if '!miku' in resp:
        resp = resp.replace('!miku', '')
        with open(filePath + str(count) + ".txt", 'w') as f:
            f.write(resp)
        count += 1
        print(resp)


