'''
- Exercici 1
L'exercici consisteix a crear una funció que et classifiqui una variable numèrica en funció de l’escala Suspès/Aprovat/Notable/Excel·lent.

Recorda que Suspès < 5, Aprovat > 5 i < 7, Notable > 7 i < 9 i Excel·lent > 9.
'''

def notes(nota):
    if nota < 5: 
        return "Suspès"
    elif nota >= 5 and nota <7: 
        return "Aprobat"
    elif nota >= 7 and nota < 9:
        return "Notable"
    else: 
        return "Excelent"

resultat_1 = notes(7)
print(resultat_1)

''' Exercici 2
Utilitzant el següent tutorial crea una funció que et pregunti dos números. T’ha de mostrar un missatge dient si el primer és més gran, el segon és més gran o són iguals.'''

'''var1 = input("Introdueix el primer número a comparar:\n")
var2 = input("Introdueix el segon número a comparar:\n")
             
def comparar_numeros(num1: int, num2: int):
    if num1 > num2:
        return f"El primer numero, el {num1} es mes gran que el segon número el {num2}"
    elif num1 < num2:
        return f"El segon numero, el {num2} es mes gran que el primer número el {num1}"
    else:
        return f"El nombres son iguals"

resultat_2 = comparar_numeros(var1, var2)
print(resultat_2)'''

'''- Exercici 3
Crea una funció que et pregunti el teu nom, i et demani un número. Si el número és 0, hauria de mostrar un missatge d’error. En cas contrari, hauria de mostrar el nom repetit tants cops com indiqui el número. Per exemple, “Joan Joan Joan”.
'''

nom = input("Introdueix en nom:\n")
num_de_noms = int(input("Introdueix el número de vegades que vols que es repeteixi el nom:\n"))

def noms_repetits(nom: str, num_de_noms: int):
    if num_de_noms == 0:
        return "Error, has indicat 0 vegades"
    else:
        return f"{nom} " * num_de_noms
    
resultat3 = noms_repetits(nom, num_de_noms)
print(resultat3)
