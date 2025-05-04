#Zadanie 1

Sklepy = {
    "piekarnia": ["Chleb", "Pączek", "Bułki"],
    "warzywniak": ["Marchew", "Seler", "Rukola"]
}

for i in Sklepy.keys():

    print (f"Idę do {(i.capitalize())} i kupuję tam {Sklepy[i]} ")
    r = Sklepy.get(i)
    X = r+r

    
print (f"W sumie kupuję {(len(X))} produktów")


#Zadanie 2
Zbior = []
for i in range (101):
    if i%5 ==0:
        Zbior.append(i)
print (Zbior)
dop = [Zbior**3 for Zbior in Zbior]
print (dop)

print ("'martwa papuga' - najlepszyt skecz")
