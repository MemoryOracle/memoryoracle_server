#!/usr/bin/env python
# -*- encoding UTF-8 -*-

import tornado.ioloop
import tornado.web
import tornado.websocket


class EchoWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print("message is {}".format(message))
        self.write_message("You said: " + message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        print(origin)
        return True


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


if __name__ == "__main__":
    application = tornado.web.Application([(r"/websocket", EchoWebSocket),])
    application.listen(8888, '::1')
    tornado.ioloop.IOLoop.current().start()


