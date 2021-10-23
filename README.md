# Projet-6

AUTOMATISATION DE CREATION DE COMPTES AD DEPUIS UNE LISTE CSV

Fonctionnement du verisonning:
- le numéro de version se trouve en commentaire en début du script
- modification mineure (court terme et moyen terme): incrémenter le version de +0.1
- modification majeure (long terme ou modfification critique): incrémenter la version à la valeur entière supérieure

Pré-requis:
- le script doit être executé en console administrateur
- le script doit être lancé depuis un serveur ayant le rôle AD déjà installé

Infomation:
- le fichier csv de données utilisateur devra contenir uniquement 2 types d'informations: noms et prénoms
- quelques informations du script sont à personnaliser au sein de votre infra (voir use-case)


I. Documentation (voir le fichier use-case pour plus de détails)
Le script est construit en plusieurs parties:
- import de modules
- lecture et manipulation de fichier csv
- transformation du fichier csv en listes de listes
- identification de doublons potentiels
- création des comptes AD

II. Limitation:
- mot de passe en clair dans le script
- l'identification des doublons dans le tableau n'est pas récursif (limité à 2 passages à ce jour)
- l'incrémentation de caractère dans l'identifiant pour éviter les doublons dans l'AD n'est pas une bonne pratique
	- il serait préférable de faire +1 plutôt qu'ajouter un caractère

III.To Do
Pistes d'amélioration:
- Court terme:
	- Supprimer le mot de passe dans le script
- Moyen terme:
	- incrémenter les identifiants du tableau quelque soit le nombre de doublons potentiels (à l'aide de l'expression "regex"??)
	- Si identifiant existe : incrémenter le dernier caractère de +1 à l'aide de l'expression régulière regex, sinon: le créer
- Long terme:
	- Ajouter un module Ansible qui crée le rôle AD lorsqu'il n'est pas installé avant de lancer le script
     	 - Documenter le projet en anglais pour toucher un plus large public