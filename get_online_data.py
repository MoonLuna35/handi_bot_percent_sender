#
#   dev's Twitter : @__MoonLuna__
#   project : handi bot petition for the AAH
#
###################################################
from datetime import date, datetime
import lxml.html
import urllib.request

import error
import utilitaries

def get_online_data():
    page = urllib.request.urlopen('https://petitions.assemblee-nationale.fr/initiatives/i-358')  # On vas sur le site de la pétition
    str_dom = page.read()  # On le lit

    root = lxml.html.fromstring(str_dom)  # On le formate en DOM
    for elem in root.xpath("//span"):  # POUR tout élément dans le DOM de type "span" FAIRE
        if "progress__bar__number" in elem.classes:  # SI l'élément courant contient le nombre de signature ALORS
            nb = int(elem.text_content().replace(" ", ""))  # On l'assigne au nombre de signature
    return nb



