import socket

def f1():
    return b'f1'
def f2():
    return b'f2'
routers = [
    ('/xxx',f1),
    ('/ooo',f2),
]


def run():
    sock = socket.socket()
    sock.bind(('127.0.0.1',8888))
    sock.listen(5)

    while True:
        conn,addr = sock.accept() #hang on
        #有人来连接
        #获取用户发送的数据
        data = conn.recv(8096)
        data = str(data,encoding='utf-8')
        headers,bodys = data.split('\r\n\r\n')
        temp_list = headers.split('\r\n')
        method,url,protocol = temp_list[0].split('')
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        func_name = None
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break

        if func_name:
            response = func_name()
        else:
            response = '404'

        conn.send(response)
        conn.close()