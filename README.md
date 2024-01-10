# Documentation du Projet

## Structure du Projet

Le projet de calculatrice est organisé de manière simple, avec un fichiers principaux :

- `main.py` : Contient le script principal où l'utilisateur interagit avec la calculatrice , Définit la classe Calculatrice avec les différentes opérations mathématiques.

## Choix Techniques

Le projet a été développé en utilisant Python en raison de sa simplicité et de sa flexibilité. La conception orientée objet a été adoptée pour encapsuler les fonctionnalités de la calculatrice dans une classe. Cela rend le code plus lisible, réutilisable et extensible.

## Bibliothèques/Frameworks Utilisés

Aucune bibliothèque externe n'a été utilisée dans ce projet, car les opérations de base ne nécessitaient pas de fonctionnalités avancées. Cependant, des bibliothèques tierces pourraient être envisagées pour des fonctionnalités futures, telles que l'interface utilisateur graphique (GUI).

## Défis Rencontrés et Solutions Apportées

### Gestion des Erreurs

Un défi majeur était la gestion des erreurs utilisateur, en particulier lors de la saisie des nombres. Pour résoudre cela, des blocs `try` et `except` ont été utilisés pour capturer les erreurs de type lors de la conversion des entrées utilisateur en nombres.

### Division par Zéro

Un autre défi était la division par zéro. Pour éviter cela, une vérification a été ajoutée avant d'effectuer la division, avec un message d'erreur approprié en cas de tentative de division par zéro.

