import csv
import shutil


with open('fichier_brut.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)


#copier fichier_brut vers fichier_final
source=r'C:\Users\Greg\Documents\Formations\INFO\OCR\Admin infra et cloud\PROJETS\Projet 6\fichier_brut.csv'
destination=r'C:\Users\Greg\Documents\Formations\INFO\OCR\Admin infra et cloud\PROJETS\Projet 6\fichier_final.csv'
shutil.copyfile(source, destination)

