###########
#Exercice 1
###########

#Programme 1
x=0
i=1
borne=int(input("borne ?"))
print("la borne est " + str(borne))
while i <= borne :
    x=x+i
    i=i+1
print(str(x)+" "+str(i))

#Programme 2
x=0
i=1
borne=int(input("borne ?"))
while i<= borne and x<10 :
    x=x+i
    i=i+1
print(x)

###########
#Exercice 2
###########
n=int(input("n ?"))
resu=n**n
print("Résultat=" + str(resu))

###########
#Exercice 3
###########
from random import randint
n=randint(0,20)

while n%4!=0 and (n<=10 or n%3==0) :
    n=randint(0,20)
print(n)

###########
#Exercice 4
###########
liVal= [8.8,1995,[1,2,3],"vacances",2005]
ch="stl"

print(liVal[-1])
print(liVal [2:4])
print(liVal[4:])
for i in liVal[2] :
    print(i*i)
val=liVal[3]
print(val[1:3])
print(liVal[3][1])
print(liVal[3][10])
print(ch[1]*3)
print(ch.append("s"))


ui=[1,2,3]
uiii=str(ui)
nop=''
for i in ui :
    nop=nop+str(i)
print(nop)
###########
#Exercice 5
###########
for i in range (1,4):
    print(i,":",end="")
    for j in range(i,4*i+1,i):
        print(j," ",end="")
    print("")
print(i,j)

###########
#Exercice 6
###########
n=int(input("quel est votre n?"))

MoyennePositif=0
SommePositif=0
NombreDePositif=0

MoyenneNegatif=0
SommeNegatif=0
NombreDeNegatif=0

PlusGrandNombre=0

while n!=0 :
    nb=int(input("votre nombre?"))
    if nb>0:
        SommePositif=SommePositif+nb
        NombreDePositif=NombreDePositif+1
        if nb>PlusGrandNombre:
            PlusGrandNombre=nb
    elif nb<0 :
        SommeNegatif=SommeNegatif+nb
        NombreDeNegatif=NombreDeNegatif+1
    n=n-1

if NombreDePositif>0 :    
    MoyennePositif=SommePositif/NombreDePositif
    print("La moyenne des positifs est: "+str(MoyennePositif))
    print("Le max est:"+str(PlusGrandNombre))
    
if NombreDeNegatif>0 :    
    MoyenneNegatif=SommeNegatif/NombreDeNegatif
    print("La moyenne des négatifs est: "+str(MoyenneNegatif))
    


###########
#Exercice 7
###########
b1=int(input("b1?"))
b2=int(input("b2?"))

if abs(b1-b2)<=20 :
    if b1-b2>0 :
        for i in range(b1,b2-1,-1):
            print(i,"",end="")
    if b1-b2<0 :
        for i in range(b1,b2+1) :
            print(i,"",end="")
    if b1==b2 :
        print(b1)
else :
    print("Ecart trop grand")




###########
#Exercice 8
###########
n=int(input("n?"))
n1=int(input("n1"))
n2=int(input("n2?"))
if n<=0 :
    print("Error n<=0")
if n1>n2 :
    print("Error n1>n2")
i=n1
while i<=n2:
    j=1
    while j<=n:
        print(i*j,end="")
        j=j+1
    print()
    i=i+1













