#!usr/bin/env python
#-*- coding:utf-8 _*-
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

USER_list = []
class ChatConsumer(WebsocketConsumer):


    def websocket_connect(self, message):
        """
        客户端发送请求进来，触发此方法
        :param message:
        :return:
        """
        self.accept()  # 执行accept之后代表链接成功
        USER_list.append(self)  # 将每一个链接的用户添加到列表中

    def websocket_receive(self, message):
        """
        客户端发送消息，触发此方法，并返回数据
        :param message:
        :return:
        """
        # print("msg:", message)      # msg: {'type': 'websocket.receive', 'text': '123'}
        data = message["text"]        # 获取字典中的数据

        # self.send("over")
        for user in USER_list:   # 遍历用户列表返回消息
            print(data)
            user.send(data)

    def websocket_disconnect(self, message):

        """
        客户端主动断开链接，触发此方法
        :param message:
        :return:
        """
        # 服务端触发异常 StopConsumer
        USER_list.remove(self)  # 将每一个链接的用户从列表中删除
        raise StopConsumer



 