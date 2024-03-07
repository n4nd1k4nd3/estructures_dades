

# exercici 1 - llista de llistes

trimestres = [
    ["gener", "febrer", "març"], 
    ["abril", "maig", "juny"], 
    ["juliol", "agost", "setembre"], 
    ["octubre", "novembre", "decembre"]
]


# exercici 2 - accedir a la llista

print(trimestres[0][1])
print(trimestres[0])
print(trimestres[2][2], trimestres[3][0])

# exercici 3 - nombres desordenats

llista_numeros = [5, 8, 2, 1, 19, 12, 11]

#Quants números hi ha?
print(len(llista_numeros))

#Quantes vegades apareix el número 3.
if 3 in llista_numeros:
    print(f"Si, el número 3 apareix {llista_numeros.count(3)} vegades")
else:
    print("No, el número 3 no es a la llista")


#Quantes vegades apareixen els nombres 3 i 4?
contar3 = llista_numeros.count(3)
contar4 = llista_numeros.count(4)

if contar3 and contar4 in llista_numeros:
    print(f"Si, el número 3 apareix {contar3} vegades y el número 4 apareix {contar4} vegades")
elif 3 and not 4 in llista_numeros:
    print(f"Si, el número 3 apareix {contar3} vegades y el número 4 no apareix")
elif 4 and not 3 in llista_numeros:
    print(f"Si, el número 4 apareix {contar4} vegades y el número 3 no apareix")
else:
    print("No, els números 3 y 4 no estàn a la llista")

#Quin és el número més gran?
#Quins són els 3 números més petits?
#Quin és el rang d’aquesta llista?