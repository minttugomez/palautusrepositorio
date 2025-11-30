# (vibe) Review

Avasin Githubissa seuraavanlaisen issuen:

"This application needs a user interface. It should be created with Flask and have features for creating and editing warehouses and adding or removing items. It could be just a one page app that has a list of warehouses and with a pull-down menu you can see the items it contains and add more or remove the existing ones. It should also have some feature for editing the warehouse itself."

ja assignasin sen Copilotille. Copilot loi sitten oikein hyvin toimivan Flask-käyttöliittymän, joka oli juuri toiveideni mukainen. Kuitenkaan yhdestä ominaisuudesta en tykännyt: joka kerta, kun varaston tietoja muutti, redirect aiheutti varasto-valikon sulkeutumisen. Tein siis Copilotille seuraavanlaisen muutosehdotuksen:

"Everything looks good, except the warehouse selection resets every time something is edited. Could you make it so that the selection is remembered and kept open?"

Copilot sitten korjasi tämän ongelman ja kaikki on nyt niin kuin halusinkin.

Copilot ylitti odotukseni tekemällä toimivan, hyvän käyttöliittymän. Koodi on hyvin selkeää. Koodissa ei korostu mikään asia, mikä ei olisi minulle ennestään tuttua, mutta uskon voivani oppia siitä, mikäli syvennyn siihen tarkemmin.