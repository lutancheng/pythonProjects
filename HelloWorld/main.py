# -*- coding: utf-8 -*-
# filename: main.py
import web
import os
root = os.path.dirname(__file__) 
render = web.template.render(os.path.join(root, '3dSpin/'), cache=False)
urls = (
    '/wx', 'Handle',
)

#render=web.template.render('3dSpin', cache=False)

class Handle(object):
    def GET(self):
        #return "hello, this is handle view"
        return render.index()

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()