# Projet-6

AUTOMATISATION DE CREATION DE COMPTES AD DEPUIS UNE LISTE EXCEL

Fonctionnemnet du verisonning:
- le numéro de version se trouve en commentaire en début du script
- modification mineure (court terme et moyen terme): incrémenter le version de +0.1
- modification majeure (long terme ou modfification critique): incrémenter la version à la valeur entière supérieure

Pré-requis:
- le script doit être executé en console administrateur
- le script doit être lancé depuis un serveur ayant le rôle AD déjà installé

Infomation:
- Les fichiers annexes (xls et csv) sont là à titre d'exemple et ne sont pas des fichiers de prod
- Donc quelques informations du script sont à personnaliser au sein de votre infra


I. Documentation
Le script est construit en plusieurs parties:
- import de modules
- lecture et manipulation de fichier excel
- transformation du fichier csv en listes de listes
- identification de doublons potentiels
- création des comptes AD

II. Limitation:
- mot de passe en clair dans le script
- l'identifiaction des doublons se fait uniquement sur le nouveau fichier identifié dans le script et non pas dans l'AD exisant

III.To Do
Pistes d'amélioration:
- Court terme:
	- Supprimer le mot de passe dans le script
- Moyen terme:
	- vérifier si ID existe dans l'AD et dans le fichier avant de procéder à la création du compte
	- Si identifiant existe : incrémenter le dernier caractère de +1 à l'aide de l'expression régulière regex, sinon: le créer
- Long terme:
	- Ajouter un module Ansible qui crée le rôle AD lorsqu'il n'est pas installé
      - Documenter le projet en anglais pour toucher un plus large public