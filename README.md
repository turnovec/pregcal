Pregnancy Calendar
==================

Program pro zobrazení kalendáře, zachycujícího celou graviditu. Vstupem je nějaké datum a k němu odpovídající gestační stáří. Typicky například stáří plodu dle biometrie (CRL, BPD) a k němu datum tohoto ultrazvukového vyšetření.

Program je napsaný v jazyce [Python](http://www.python.org/), funguje jako webová aplikace a pro jeho spuštění je nutné mít nainstalovaný minimalistický framework [Flask](http://flask.pocoo.org/).

Program je možné spustit přímo - pregcal.py - pak je vytvořen lokální webový server na portu 5000. Je ale samozřejmě možné ho pustit i jako WSGI aplikaci a tu pak schovat za nějaký "plnotučný" webový server jako například [Nginx](http://nginx.org/) nebo [Apache](http://httpd.apache.org/).
