# klases nosaukums vienmér ar Lielo burtu(Shoes),
# bet  faila nosaukums ar mazo!(extracode.py)
class Shoes:

    # klases atribúti
    materials = "leather"
    tips = "High heels"

    # objektu atribúti.
    # Inicializacijas funkcija, vienmér klasé
    def __init__(self, dizaineris, cena, atlaide):
        #objekts sev pieskir padotas vertibas
        self.dizaineris = dizaineris
        self.cena = cena
        self.atlaide = atlaide

    def myFirstClassFunction(self):
        return "Hi! This is shoes looks good"

    def mySecondClassFunction(self):
        return "These shoes are too expensive"

    #cenas mainígá vértíbas atgriesanai
    def getPrice(cena):
        return cena


# extracode funkcijas arpus Shoes klases
def functionOutsideClass():
    return "Ï dont give a damn about shoes"