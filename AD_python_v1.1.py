#VERSION V1.7

#importer les packages nécessaires
import csv
import shutil
import numpy as np
from pyad import *


#Lit le fichier csv de base
with open('fichier_brut.csv', encoding='utf-8') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)


#copier fichier_brut vers fichier_temp1
source=r'C:\Users\mon\Fichier\brut.csv'
destination=r'C:\Users\mon\Fichier\fichier_temp1.csv'

shutil.copyfile(source, destination)



#transformer fichier_temp1 en tableau (en listes de listes)
Tableau = []
Prenom = []
Nom = []

# Lit le fichier temp1
with open('fichier_temp1.csv', encoding='utf-8') as fichier_csv:
    #ATTENTION AU CHOIX DU DELIMITEUR!!!!
    reader = csv.reader(fichier_csv, delimiter=';')
        #row --> met le tableur sous forme de listes de listes ; Tableau =[[prenom1, nom1],[prenom2,nom2]...]
    for row in reader:
            Tableau.append(row)
    fichier_csv.close

#contrôler qu'on est passé en mode liste de liste
#print(Tableau)

#créations de variables: nommer une colonne et initialiser compteur
ajout_colonne='identifiant'
i=0

#Ajouter colonne au tableau
for row in Tableau:
    row.append(ajout_colonne)


#recherche de doublon dans les identifiants
RechDoublon={}
for i in range(len(Tableau)):
    
    if i==0:
        Tableau[i]=[Tableau[i][0],Tableau[i][1], 'Identifiants']
    else:
        Tableau[i]=[Tableau[i][0],Tableau[i][1],'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'1']
        if 'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'1' in RechDoublon:
          Tableau[i]=[Tableau[i][0],Tableau[i][1], 'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'2']
          print('Attention')
        else:
           print('OK')
        RechDoublon['u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'1']=[Tableau[i][0],Tableau[i][1],'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'1']

#2eme recherche de doublons
RechDoublon2={}
for i in range(len(Tableau)):
    if Tableau[i]==[Tableau[i][0],Tableau[i][1],'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'2'] and Tableau[i-1]==[Tableau[i-1][0],Tableau[i-1][1],'u'+Tableau[i-1][0][0]+Tableau[i-1][1][0:3]+'2']:
        Tableau[i]=[Tableau[i][0],Tableau[i][1], 'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'3']
        print('Attention')
    else:
        print('OK')


#Supprimer la première ligne qui correspond aux titres des colonnes
del Tableau[0]


#préparer le module pyad: définir le compte admin pour faire les manip auto
pyad.set_defaults(ldap_server="ADPython.com", username="Administrateur", password="xxxxxxxxxx")
ou=pyad.adcontainer.ADContainer.from_dn("ou=Groupes, dc=ADPython, dc=com")

#####CONTROLER DOUBLON DE L'AD :evolution a etudier
#n=1
#for i in range(len(Tableau)):
#       Tableau[i]=[Tableau[i][0],Tableau[i][1],'u'+Tableau[i][0][0]+Tableau[i][1][0:3]]
#       while 'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+str(n) in ou:
#           n=n+1
#           Tableau[i]=[Tableau[i][0],Tableau[i][1],'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+str(n)]
#       Tableau[i]=[Tableau[i][0],Tableau[i][1],'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'1']


#ajouter les utilisateurs en lisant le csv:
new_group=pyad.adgroup.ADGroup.from_cn('employee')
new_user=[]
for row in Tableau:
    givenName=row[0]
    name=row[1]
    sAMAccountName=row[2]
    print(givenName, name, sAMAccountName)
    new_user.append(pyad.aduser.ADUser.create(sAMAccountName, ou, 'xxxxxxxxxxx', optional_attributes={"givenName":givenName, "displayName":name+' '+givenName, "sn":name}))
    
new_group.add_members(new_user)

print('Les comptes utilisateurs ont été créés')

