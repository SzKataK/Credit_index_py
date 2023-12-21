# Credit index counter / kreditindex számoló

## Summary in English

Credit index counter console app for ELTE University (Hungary) students.

Programming language: Python

Language: Hungarian

## Leírás

Kreditindex számoló console app ELTÉ-seknek a [2017-es HKR alapján](https://www.elte.hu/dstore/document/898/ELTE_SZMSZ_II_170530.pdf).

Programozási nyelv: Python

## Mit számol?

- Kreditindex (KI)
- Korrigált kreditindex (KKI)
- Teljesített kredit
- Hagyományos átlag
- Súlyozott átlag (TÁ)

[A számolások menete részletesen](itcounts.md)

## Használat

### Általános összefoglaló fájlból olvasáshoz

1. Neptun -> Tárgyak -> Felvett tárgyak
2. Másold át a tartalmat egy txt-be és mentsd el a `grades` mappába
3. Az első futtatás után jelezni fogja, hogy írd be a jegyeket a tárgyakhoz
4. Futtasd le újra
5. Az eredmények megjelennek a konzolon és a `results` mappában

#### A jegyeket tartalmazó fájl helyes formátuma

Tárgy név;kredit;jegy

(Ne legyen benne üres sor! Dolgozok a hiba kijavításán.)

### Parancssori argumentummal

`python .\src\main.py "fajlnev"`

Add meg a fájl nevét!

### Konzol

`python .\src\main.py`

Beolvashatsz fájlból vagy megadhatod konzolban az adaotokat
