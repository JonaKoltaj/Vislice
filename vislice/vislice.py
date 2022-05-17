import bottle, model

SKRIVNOST = "Analiza je najboljši predmet"

vislice = model.Vislice()
vislice.nalozi_igre_iz_datoteke()

@bottle.get("/")
def indeks():
    return bottle.template("views/index.tpl")

@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', id_igre, path="/", secret=SKRIVNOST)
    vislice.zapisi_igre_v_datoteko()
    return bottle.redirect("/igra/")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    igra, stanje = vislice.igre[id_igre]
    geslo = igra.pravilni_del_gesla()
    nepravilni = igra.nepravilni_ugibi()
    obesenost = igra.stevilo_napak()
    celo_geslo = igra.geslo

    return bottle.template("views/igra.tpl", {'stanje': stanje, 'model': model, 'geslo': geslo, 'celo_geslo': celo_geslo, 'nepravilni': nepravilni, 'obesenost': obesenost})

@bottle.post("/igra/")
def ugibaj():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNOST)
    crka = bottle.request.forms.crka
    vislice.ugibaj(id_igre, crka)
    vislice.zapisi_igre_v_datoteko()
    return bottle.redirect("/igra/")

@bottle.get("/img/<picture>")
def slike(picture):
    return bottle.static_file(picture, root="img")


bottle.run(reloader=True, debug=True)