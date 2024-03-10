'''
- Exercici 1
L'exercici consisteix a crear una funció que et classifiqui una variable numèrica en funció de l’escala Suspès/Aprovat/Notable/Excel·lent.

Recorda que Suspès < 5, Aprovat > 5 i < 7, Notable > 7 i < 9 i Excel·lent > 9.
'''

# Exercici 1 funcio

def notes(nota):
    if nota < 5: 
        return "Suspès"
    elif nota >= 5 and nota <7: 
        return "Aprobat"
    elif nota >= 7 and nota < 9:
        return "Notable"
    else: 
        return "Excelent"

primera_nota = notes(7)
print(primera_nota)