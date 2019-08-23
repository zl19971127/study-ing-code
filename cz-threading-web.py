# _*_ coding:utf-8 _*_
# author: zl
# time: 19-08-23
# python: 3.6.2

# 导入模块 - 套接字socket和线程threading
import socket
import threading
# 加一个全局变量i判断每个客户端访问次数
i = 0


def function(main_socket):
    # 加一个死循环，使服务器不断的运行，而不是只运行一次，只要客户不断，服务器就不能断开
    while True:
        global i
        i += 1
        # 调用accept方法，得到客户端的P加端口，和自己返回的一个连接客户端的套接字，用元组封装
        user_socket, user_address = main_socket.accept()
        print("%s地址的机器第%s次访问了您的服务器！" % (str(user_address), i))
        # 使用recv这个方法，接收客户的数据，以请求报文的形式传输进来且为二进制,用decode方法转码
        user_data = user_socket.recv(4096).decode()
        print("客户端传来的请求报文:\r\n" + user_data)
        # print(user_data) 测试运行成功
        try:
            # 暂会 用户以 GET方式传来数据则，用spilt方法用特定符号分割开，放入列表中，取出需要的部分
            request_data = user_data.split("\r\n")[0].split(" ")[1]
        except Exception as e:
            request_data = "/01.gif"
        else:
            pass
        finally:
            pass
        # 如果用户没有请求数据时，默认跳转到01.gif上
        if request_data == "/":
            request_data = "/01.gif"
        # 如果用户输入一个没有的文件就用异常处理，抛出404
        try:
            # 暂会 需要一个文件夹，里边有数据，读取文件夹中的数据，传给用户
            with open("image" + request_data, "rb") as file:
                send_data = file.read()
                # 传输需要以响应报文的形式传输，否则客户端不识别
                http_message = "HTTP1.1 200 OK\r\n\r\n"
        except Exception as e:
            with open("image/404.html", "rb") as file:
                send_data = file.read()
                # 需要将响应报文中的状态码和状态说明修改
                http_message = "HTTP1.1 404 not found\r\n\r\n"
        else:
            pass
        finally:
            # 调用send方法给客户端传数据
            user_socket.send(http_message.encode() + send_data)
            # 关闭该套接字
            user_socket.close()


def main():
    # 创建监听的套接字
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 使程序关闭在开时套接字的端口可以复用，不用在等待或者换端口
    main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 调用bind()方法，设定该服务器的IP和端口,（元组形式）
    main_socket .bind(("", 80))
    # 调用listen()方法，这是监听的方法，表示同一时间有多少可以一起等待，一般是128
    main_socket.listen(128)

    # 创建线程对象,使线程调用function函数，来完成功能
    web_thread = threading.Thread(target=function, args=(main_socket, ))
    # 启动线程
    web_thread.start()


if __name__ == "__main__":
    main()
