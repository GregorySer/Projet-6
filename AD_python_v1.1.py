#VERSION V1.8

#importer les packages nécessaires
import csv
import shutil
import numpy as np
import pyad.adquery
from pyad import *

#Lit le fichier csv de base
with open('fichier_brut.csv', encoding='utf-8') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')

try:
    #copier fichier_brut vers fichier_temp1
    source=r'C:\Users\mon\Fichier\brut.csv'
    destination=r'C:\Users\mon\Fichier\fichier_temp1.csv'

    shutil.copyfile(source, destination)
except:
        print('Erreur dans le chemin du fichier source ou de destination')

#déclaration de variables
q = adquery.ADQuery()
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

#Déclarer nouvelle variable
ajout_colonne='identifiant'

#initialiser variable
i=0

#Ajouter colonne au tableau
for row in Tableau:
    row.append(ajout_colonne)


#recherche de doublon dans Tableau
RechDoublon={}
for i in range(len(Tableau)):
    
    if i==0:
        Tableau[i]=[Tableau[i][0],Tableau[i][1], 'Identifiants']
    else:
        Tableau[i]=[Tableau[i][0],Tableau[i][1],'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'1']
        if 'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'1' in RechDoublon:
          Tableau[i]=[Tableau[i][0],Tableau[i][1], 'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'2']
        else:
        RechDoublon['u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'1']=[Tableau[i][0],Tableau[i][1],'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'1']

#Supprimer la première ligne qui correspond aux titres des colonnes
del Tableau[0]

#2eme recherche de doublons dans Tableau
RechDoublon2={}
for i in range(len(Tableau)):
    if Tableau[i]==[Tableau[i][0],Tableau[i][1],'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'2'] and Tableau[i-1]==[Tableau[i-1][0],Tableau[i-1][1],'u'+Tableau[i-1][0][0]+Tableau[i-1][1][0:3]+'2']:
        Tableau[i]=[Tableau[i][0],Tableau[i][1], 'u'+Tableau[i][0][0]+Tableau[i][1][0:3]+'3']
        #tant qu'il y a un "attention" il y a des doublons dans le tableau
        print('Attention')
    else:
        print('OK')


try:
    #préparer le module pyad: définir le compte admin pour faire les manip auto
    pyad.set_defaults(ldap_server="xxxxxxxx", username="xxxxxx", password="xxxxxxxxxx")
    ou=pyad.adcontainer.ADContainer.from_dn("ou=xxxxx, dc=xxxxx, dc=xxx")
except:
    print('Vérifier si le compte, le domaine, l\'OU existent et si le mot de passe est correct')
    

#ajouter les utilisateurs en lisant la liste de listes et contrôle des doublons dans l'AD avec ADQuery et boucle while
new_group=pyad.adgroup.ADGroup.from_cn('xxxxxx')
new_user=[]
for row in Tableau:
    givenName=row[0]
    name=row[1]
    sAMAccountName=row[2]
    inserted=0
    while inserted!=1:
 
        q.execute_query(
                attributes = ["distinguishedName", "sAMAccountName"],
                where_clause = "objectClass = 'user'",
                base_dn = "ou=xxxx, dc=xxxxx, dc=xxx"
        )
        found = 0
        for row in q.get_results():
            if row["sAMAccountName"] == sAMAccountName:
                    found = 1
        if not found:
             new_user.append(pyad.aduser.ADUser.create(sAMAccountName, ou, 'Azerty1234+', optional_attributes={"givenName":givenName, "displayName":name+' '+givenName, "sn":name}))
             inserted=1
        else:
              sAMAccountName=sAMAccountName+'1'
new_group.add_members(new_user)


print('Les comptes utilisateurs ont été créés')
