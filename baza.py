import csv

PARAM_FMT = ":{}" # za SQLite

class Tabela:
    """
    Razred, ki predstavlja tabelo v bazi.

    Polja razreda:
    - ime: ime tabele
    - podatki: ime datoteke s podatki ali None
    """
    ime = None
    podatki = None

    def __init__(self, conn):
        self.conn = conn
    
    def ustvari(self):
        """Ustvari tabelo v bazi.

        Podrazredi morajo povoziti to metodo.
        """
        raise NotImplementedError
    
    def izbrisi(self):
        """Izbriše tabelo."""
        self.conn.execute(f"DROP TABLE IF EXISTS {self.ime};")
    
    def dodajanje(self, stolpci=None):
        """
        Metoda za gradnjo poizvedbe.

        Argumenti:
        - stolpci: seznam stolpcev
        """
        return f"""
            INSERT INTO {self.ime} ({", ".join(stolpci)})
            VALUES ({", ".join(PARAM_FMT.format(s) for s in stolpci)});
        """

    def dodaj_vrstico(self, **podatki):
        """
        Metoda za dodajanje vrstice.

        Argumenti:
        - poimenovani parametri: vrednosti v ustreznih stolpcih
        """
        podatki = {kljuc: vrednost for kljuc, vrednost in podatki.items()
                   if vrednost is not None}
        poizvedba = self.dodajanje(podatki.keys())
        cur = self.conn.execute(poizvedba, podatki)
        return cur.lastrowid

    def uvozi(self, encoding="UTF8"):
        if self.podatki is None:
            return None
        with open(self.podatki, encoding=encoding) as datoteka:
            podatki = csv.reader(datoteka)
            stolpci = next(podatki)
            for vrstica in podatki:
                podatek = {k: None if v == "" else v for k, v in zip(stolpci, vrstica)}
                self.dodaj_vrstico(**podatek)

class Stranka(Tabela):
    """Tabela s podatki o strankah."""
    ime = "stranka"
    podatki = "podatki/stranke.csv"

    # Init dela isto kot konstruktor razreda Tabela,
    # zato ga ni potrebno ponovno implementirati in se bo
    # klical avtomatsko.

    def ustvari(self):
        """Ustvari tabelo stranka."""
        sql = """
            CREATE TABLE stranka (
                id  INTEGER PRIMARY KEY,
                ime TEXT NOT NULL UNIQUE
            );
        """
        self.conn.execute(sql)

class Narocilo(Tabela):
    ime = "narocilo"
    podatki = "podatki/narocila.csv"

    def ustvari(self):
        """Ustvari tabelo narocilo."""
        sql = """
            CREATE TABLE narocilo (
                id          INTEGER PRIMARY KEY,
                kolicina    INTEGER CHECK (kolicina > 0),
                stranka     INTEGER REFERENCES stranka(id)
            );
        """
        self.conn.execute(sql)


def pripravi_bazo():
    conn = sqlite3.connect("baza.sqlite")
    stranka = Stranka(conn)
    narocilo = Narocilo(conn)
    stranka.izbrisi()
    narocilo.izbrisi()
    stranka.ustvari()
    narocilo.ustvari()
    stranka.uvozi()
    narocilo.uvozi()
    stranka.dodaj_vrstico(**{"ime":"Gregor"})
    conn.commit()

    conn.close()
                          
if __name__ == "__main__":
    import sqlite3
    pripravi_bazo()