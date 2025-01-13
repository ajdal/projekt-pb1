import sqlite3

conn = sqlite3.connect("baza.sqlite")

class Stranka:

    def __init__(self, ime, id_stranke):
        self.id_stranke = id_stranke
        self.ime = ime

    def __repr__(self):
        return f"Stranka({self.ime})"
    
    def __str__(self):
        return self.ime
    
    @staticmethod
    def vse_stranke():
        poizvedba = """SELECT id, ime FROM stranka"""
        for id_stranke, ime in conn.execute(poizvedba):
            yield Stranka(ime, id_stranke)

    @staticmethod
    def najdi_stranko(id_stranke):
        poizvedba = """SELECT id, ime FROM stranka WHERE id = ?"""
        id_stranke, ime = conn.execute(poizvedba, [id_stranke]).fetchone()
        return Stranka(ime, id_stranke)

class Narocilo:

    def __init__(self, id_narocila, id_stranke, kolicina):
        self.id_narocila = id_narocila
        self.id_stranke = id_stranke
        self.kolicina = kolicina
    
    @staticmethod
    def narocila_stranke(stranka):
        poizvedba = """
        SELECT id, kolicina
        FROM narocilo
        WHERE stranka = ?
        """
        for id_narocila, kolicina in conn.execute(poizvedba, [stranka.id_stranke]):
            yield Narocilo(id_narocila, stranka.id_stranke, kolicina)