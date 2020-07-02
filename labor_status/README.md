# Laborstatus

[Das Labor](https://das-labor.org) ist ein Hackspace in Bochum.
Über das Skript soll ausgegeben werden, ob das Labor gerade geöffnet ist oder 
nicht.

Es kann einfach aufgerufen werden und benötigt keine Parameter.

    $ python3 labor_status.py
    OPEN


## Test

Das Skript enthält eine Methode und einen Test im Methodenkommentar. Mit dem 
Modul `doctest` kann es ausgeführt werden.

    python3 -m doctest labor_status.py
