import model
import bottle
from bottle import route, run, Response, template

app = bottle.default_app()

#@route('/')
#def tittle():
#    return Response("PORABA GORIVA")


@route('/')
def index():
    return bottle.template('index.tpl')


bottle.run(reloader=True, debug=True)






