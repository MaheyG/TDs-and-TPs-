###############
#EXERCIE WHILE#
###############

n=89
i=0
nmax=0
while n!=1 :
    if n%2==0 :
        n=n/2
    else:
        n=3*n+1
    i=i+1
    if n>nmax :
        nmax=n
    print(n)



#Limité l'altitude à 150
n=135
nmax=n
while n!=1 :
    if n%2==0 :
        n=n/2
    else:
        n=3*n+1
    if n>nmax :
        nmax=n
    print(n)
print(nmax)

#Limité le temps de vol à 30 et l'altitude à 1000
n=89
i=0
while n!=1 and n<1000 and i<30 :
    if n%2==0 :
        n=n/2
    else:
        n=3*n+1
    i=i+1
    print(n)
print("i=",i) 

#Continué tant que le temps de vol ET l'altitude max ne sont supérieur à 600 et 60
n=123
i=0
nmax=n
while n!=1 and (nmax<600 or i<60) :
    if n%2==0 :
        n=n/2
    else:
        n=3*n+1
    if n>nmax:
        nmax=n
    i=i+1
    print(n)
print("i=",i) 

###############
#EXERCICE LIST#
###############
liVal= [45.2,1995,[1,2,3],"vacances",2005]


#Printer la taille (type?)
len(liVal)

#Printer 2005
print(liVal[-1])

#Printer [[1, 2, 3], 'vacances']
print(liVal [2:4])

#Que renvoie??
print(liVal[4:])

#Printer 1 4 9 (en colonne)
for i in liVal[2] :
    print(i*i)
#Que fait [1,2,3]*3???
    

#Remplacer 2005 par 2006
liVal[-1]=2021

#Ajoouter "éléphant" entre "vacances" et 2005
liVal=liVal[0:4]+["éléphant"]+[liVal[-1]]

#Si on sait juste que c'est avant dernier?
liVal=liVal[0:-2]+["éléphant"]+[liVal[-1]]

#Si on veut le mettre après vacance, sans connaitre les positions
i=0
while liVal[i]!= "vacances" :
    i=i+1
liVal=liVal=liVal[0:i+1]+["éléphant"]+liVal[i+1:] #Attention pas de crochet pour le dernier!!!!

#Supprimer "vacance" de la liste
del liVal[3]

#Supprimer tout les nombres de la liste
asupprimer=[]
for i in liVal :
    print(i)
    if type(i)==int or type(i)==float:
        asupprimer=asupprimer+[i]

for i in asupprimer :
    liVal.remove(i)
liVal