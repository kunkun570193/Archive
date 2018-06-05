# coding=utf-8
import tornado.options
import tornado.ioloop
import tornado.web
from tornado.options import define
import datetime
import json
from log import *

define("port", default=8035, help="run on the given port", type=int)



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("headers")
        self.set_header("Content-type","application/json; charset=UTF8")
        self.set_status(404, 'error')
        self.add_header('aaaa', '6666')

    def post(self):
        global time
        self.set_status(200)
        self.set_header("Content-type","application/json; ")
        self.add_header('fffff', '22222')
        self.write("66666")
        #获取当前时间
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(time)
        mylogger.info(time)
        #获取ip
        remote_ip = self.request.remote_ip
        print(remote_ip)
        mylogger.info(remote_ip)
        #获取url
        url = self.request.path
        print(url)
        mylogger.info(url)
        #获取数据
        data = json.loads(self.request.body.decode('utf-8'))
        print(data)
        mylogger.info(data)


settings={
    "debug":True
}

application = tornado.web.Application([
    (r"/.*", IndexHandler),
],**settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(8035)
    tornado.ioloop.IOLoop.current().start()

