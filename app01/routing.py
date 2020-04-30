#!usr/bin/env python
#-*- coding:utf-8 _*-

from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from app01 import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        url(r'^chat/$', consumers.ChatConsumer),

    ])
})

