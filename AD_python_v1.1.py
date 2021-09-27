#importer les packages nécessaires
import csv
import shutil

#Lit le fichier csv de base
with open('fichier_brut.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)


#copier fichier_brut vers fichier_temp1
source=r'C:\Users\Greg\Documents\Formations\INFO\OCR\Admin infra et cloud\PROJETS\Projet 6\fichier_brut.csv'
destination=r'C:\Users\Greg\Documents\Formations\INFO\OCR\Admin infra et cloud\PROJETS\Projet 6\fichier_temp1.csv'
shutil.copyfile(source, destination)



#transformer fichier_temp1 en tableau (en listes de listes)
Tableau = []
Prenom = []
Nom = []

# Lit le fichier temp1
with open('fichier_temp1.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
        #row --> met le tableur sous forme de listes de listes ; Tableau =[[prenom1, nom1],[prenom2,nom2]...]
    for row in reader:
            Tableau.append(row)
    fichier_csv.close

#contrôler qu'on est passé en mode liste de liste
print(Tableau)

#creer colonne "Identifiant" et fonction "f_identifiant"
titre='Identifiant'
f_identifiant=row[1]+row[0:3]+1

#creer fonction "identifiant"
ajout_colonne_identifiant('fichier_temp1.csv', 'fichier_temp_colonn.csv',
                          lambda row, line_num: row.append(titre) if line_num==1 else
                          row.append(f_identifiant))

print(fichier_temp_colonn.csv)

#on récupère les données:
#for i in range(Prenom.append(Tableau[i][0])
#        Nom.append(Tableau[i][1])
#    print(Prenom, Nom)




