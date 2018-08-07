########################
##########客户端#########
########################
import socket#导入socket库
import time, threading#导入threading模块
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建一个socket
#s.connect(('www.baidu.com', 80))#建立连接
#s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')#发送数据
##s.connect(('www.sina.com.cn', 80))#建立连接
##s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')#发送数据
##接收数据
#buffer = []
#while True:
#    #每次最多接受1kb
#    d = s.recv(1024)#一次最多接受指定的字节数
#    if d:
#        buffer.append(d)
#    else:
#        break
#data = b''.join(buffer)
##关闭连接
#s.close()
##header,html = data.split(b'\r\n\r\n',1)  #将HTTP首部和网页分离
##print(header.decode('utf-8'))
###把接收的数据写入文件
##with open('sina.html','wb') as f:
##	f.write(html);
#header, html = data.split(b'\r\n\r\n', 1)
#print(header.decode('utf-8'))
## 把接收的数据写入文件:
##with open('sina.html', 'wb') as f:
#with open('baidu.html', 'wb') as f:
#    f.write(html)
###




#######################
#########with()##########
#######################
#class Sample:
#    def __enter__(self):
#        print("in __enter__")

#        return "Foo"

#    def __exit__(self, exc_type, exc_val, exc_tb):
#					#exc_type：　错误的类型 
#					#exc_val：　错误类型对应的值 
#					#exc_tb：　代码中错误发生的位置 
#        print("in __exit__")

#def get_sample():
#    return Sample()
#with get_sample() as sample:
#    print("Sample: " ,sample)

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

	#建立连接后,服务器首先发一条欢迎消息,然后等待客户端数据,并加上Hello,xxx!再发送给客户端.入伙客户端发送了'exit'字符串,就直接关闭连接

########################
##########服务器#########
########################


#创建一个给予IPv4和TCP协议的Socket:



s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#监听端口

#绑定
s.bind(('127.0.0.1',9999))
#调用listen()函数监听端口,传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection...')
#服务器通过一个死循环来接受来自客户端的链接,accept()会等待并返回一个客户端的链接:
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
#每个链接都必须创建新线程(或进程)来单独处理,否则,单线程在处理连接的过程中,无法接受其他客户啊短的链接:




