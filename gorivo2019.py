import model
import bottle
from bottle import route, run, Response, template

app = bottle.default_app()

#@route('/')
#def tittle():
#    return Response("PORABA GORIVA")

gorivo = model.Model()


@route('/')
def index():
    return bottle.template('index2.html')

@bottle.post('/')
def vnesi():
    gorivo.vnesi_tank({'datum': bottle.request.forms.get('datum'), 'tank': bottle.request.forms.get('tank'), 'stanje': bottle.request.forms.get('stanje'), 'cena': bottle.request.forms.get('cena')} )
    bottle.redirect('/')

@bottle.get('/prikazi_zgodovino/')
def zgodovina():
    zgo = gorivo.prikazi_zgodovino()
    print(zgo)
    return bottle.template('zgodovina.html', gorivo = zgo)

@bottle.get('/delete/')
def razveljavi_zadnji():
    gorivo.razveljavi()
    bottle.redirect('/')

@bottle.get('/reset/')
def reset():
    gorivo.reset_funkcija()
    bottle.redirect('/')


bottle.run(reloader=True, debug=True)






