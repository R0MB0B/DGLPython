job1=False
while job1==True:
    f = open("output.txt", 'w')
    chaine=input("chaine de caractère ")
    f.write(str(chaine))
    f.close()
    f = open("output.txt", "r")
    # print(f.read())

job2=False
while job2==True:
    f=open("output.txt","r")
    print(f.read())

import re
def nombreMots():
    data=open("data.txt","r")
    # data.read()
    espaces=re.findall("\s", data.read())
    return("Il y a "+str(len(espaces))+" mots dans data.txt")
# print(nombreMots())


def longueurMot(taille):
    data=open('data.txt','r')
    # mot="\.? ?{} ?\.?".format('.'*taille)
    # mot="\w{0}\w '+ str(taille)+' ?,?;?\??\.?"
    # mot="\w{0}\w{} ?,?;?\??\.?"
    result=re.findall("\w{0}\w{} ?,?;?\??\.?".format(taille), data.read())
    # result=re.findall(str(mot), data)
    return(result)
# print(longueurMot(4))


import matplotlib.pyplot as plt
import numpy

def compte():
    data=open('data.txt','r')
    dico={}
    n=0
    for line in data:
        line=line.lower()
        sline=line.split()
        # print(sline)
        for mot in sline:
            for lettre in mot:
                n+=1
                if str(lettre) not in dico.keys():
                    dico[str(lettre)]=1
                else :
                    dico[str(lettre)]+=1
    for key in dico.keys():
        dico[str(key)]=dico[str(key)]/n
    return(dico)

# dico=compte()
# dico=sorted(dico.items(), key=lambda t: t[1])
# # y=list(dico.values())
# y=[c[1] for c in dico]
# fig=matplotlib.pyplot.figure()
# # x=list(dico.keys())
# x=[c[0] for c in dico]
# plt.plot(x,y)
# # ax.plot(x,y)
# # x.set_title('Histogramme')
# plt.show()



def histoMots():
    data=open("data.txt","r")
    n=0
    dico={}
    for line in data:
        line=line.lower()
        sline=line.split()
        for mot in sline:
            long=len(mot)
            n+=1
            if long not in dico.keys():
                dico[long]=1
            else :
                dico[long]+=1
    for key in dico.keys():
        dico[key]=dico[key]/n
    return(dico)


# dico=histoMots()
# dico=sorted(dico.items(), key=lambda t: t[1])
# # y=list(dico.values())
# y=[c[1] for c in dico]
# # fig=plt.figure()
# # x=list(dico.keys())
# x=[c[0] for c in dico]
# # plt.plot(x,y)
# # # ax.plot(x,y)
# # # x.set_title('Histogramme')
# # plt.show()
    
# plt.hist(x, bins=y)
# plt.show()

def alphabet():
    data=open("data.txt","r")
    alpha=[]
    for line in data:
        line=line.lower()
        for lettre in line:
            if lettre not in alpha:
                alpha.append(lettre)
    return lettre

def histoSuivant():
    data=open("data.txt","r")
    lettres=alphabet
    dictionnaire={}
    for let in lettres:
        dic={}
        n=0
        for line in data:
            line=line.lower()
            sline=line.split()
            for mot in sline:
                for i in range(len(mot)-1):
                    if mot[i]==let:
                        n+=1
                        if mot[i+1] not in dic.keys():
                            dic[mot[i+1]]=1
                        else:
                            dic[mot[i+1]]+=1
        for key in dic.keys():
            dic[key]=dic[key]/n
        dictionnaire[let]=dic
    return(dictionnaire)

dico=histoSuivant()
dico=sorted(dico.items(), key=lambda t: t[1])
# y=list(dico.values())
y=[c[1] for c in dico]
# fig=plt.figure()
# x=list(dico.keys())
x=[c[0] for c in dico]
# plt.plot(x,y)
# # ax.plot(x,y)
# # x.set_title('Histogramme')
# plt.show()
    
# plt.hist(x, bins=y)
# plt.show()

fig=plt.figure()
x=fig.add_subplot(121)
x.hist(y)

d







    


       




