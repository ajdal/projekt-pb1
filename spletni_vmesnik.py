import bottle
from model import Stranka, Narocilo

@bottle.get("/stranka/<id_stranke:int>")
def narocila_stranke(id_stranke):
    stranka = Stranka.najdi_stranko(id_stranke)
    narocila = Narocilo.narocila_stranke(stranka)
    return bottle.template(
        "narocila_stranke.html", 
        stranka=stranka, 
        narocila=narocila
    )



@bottle.get("/stranke")
def seznam_strank():
    stranke = Stranka.vse_stranke()
    return bottle.template("stranke.html", osebe=stranke)


@bottle.get("/")
def index():
    return bottle.template("domov.html")


if __name__ == "__main__":
    bottle.run(debug=True, reloader=True)