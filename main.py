#importé extracode failu,
#ar as to turpmák lieto sevis izvélétá nosaukumá
#as lieto'sana nav obligáta
import extracode as sh

#izveido Shoes klases objektu
# Atceries! Funkcijai ir jápadod tik parametri,
# cik parametrus esiet noradijusi funkciju veidojot:
# def __init__(self, dizaineris, cena, atlaide)
#tátad, padodam 3 parametrus- dizaineri,cenu,atlaidi
firstShoes = sh.Shoes("Gucchi",890.45, 20)

secondShoes = sh.Shoes("Chloe", 466.99,10)
# Visiem Shoe klases objektiem ir
# klases atribúti materials un tips jau definéti:
#     materials = "leather"
#     tips = "High heels"
# Ja kádam objektam sis vertibas velaties citas, tas var parrakstit
secondShoes.materials = "suede"
print(firstShoes.materials)
print(secondShoes.materials)

#Funkcijas no extracode bibliotekas Shoes klases
print(secondShoes.myFirstClassFunction())
print(secondShoes.getPrice())

#Funkcija no extracode bibliotékas
print(sh.functionOutsideClass())






