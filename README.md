# Projet-6

AUTOMATISATION DE CREATION DE COMPTES AD DEPUIS UNE LISTE EXCEL

Pré-requis:
- le script doit être executé en console administrateur
- le script doit être lancé depuis un serveur ayant le rôle AD déjà installé


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
   Court terme:
      - Supprimer le mot de passe
   Moyen terme:
           - vérifier si ID existe dans l'AD et dans le fichier avant de procéder à la création du compte
           - Si identifiant existe : incrémenter le dernier caractère de +1 à l'aide de l'expression régulière regex, sinon: le créer
   Long terme:
      - Ajouter un module Ansible qui crée le rôle AD lorsqu'il n'est pas installé