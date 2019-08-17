import model
import bottle
from bottle import route, run, Response, template

app = bottle.default_app()

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
    cena = gorivo.cena()
    if cena > 0:
        cena = 'je podražilo.'
    elif cena < 0:
        cena = 'je pocenilo.'
    else:
        cena = 'ni podražilo.'
    analiza = [gorivo.km_tankamo(), cena, gorivo.poraba_avta()]
    return bottle.template('zgodovina.html', gorivo = zgo, analiza = analiza)

@bottle.get('/delete/')
def razveljavi_zadnji():
    gorivo.razveljavi()
    bottle.redirect('/')

@bottle.get('/reset/')
def reset():
    gorivo.reset_funkcija()
    bottle.redirect('/')

@bottle.get('/kalkulator/')
def kalkulator():
    return bottle.template('kalkulator.html', stroski = '')

@bottle.post('/kalkulator/')
def izracunaj():
    stroski = gorivo.izracun_stroskov({'razdalja': bottle.request.forms.get('razdalja'), 'poraba': bottle.request.forms.get('poraba'), 'cena': bottle.request.forms.get('cena')} )
    return bottle.template('kalkulator.html', stroski = 'Rezultat ' + str(stroski) + ' €')

bottle.run(reloader=True, debug=True)







