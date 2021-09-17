# Alien-Python

Alien-Python est à la fois une bibliothèque permettant de créer des exercices corrigés de programmation où les élèves doivent deviner la case d'arrivée d'un alien se déplaçant suivant un programme Python et à la fois une collection d'exercices basés sur cette bibliothèque. Ces exercices peuvent être utilisés pour des activités débranchées.

30 exercices de bases sont fournis. Ils sont disponibles dans les dossiers `exercices/sujets` et `exercices/corrections`.

- Les exercices 1 à 8 portent sur les déplacements et l'utilisation des variables

- Les exercices 9 à 20 portent sur les boucles de répétition.

- Les exercices 21 à 35 portent sur les conditions

La grille ci-dessous est données aux élèves :

<img src="https://user-images.githubusercontent.com/53106394/132256944-e0aa843a-f729-4e3f-8522-48c9dc8735f2.png" width="400" />

Ainsi qu'un programme Python :

![image](https://user-images.githubusercontent.com/53106394/132256741-9cd2c81c-0af4-421b-99ef-b27e183e0fd1.png)

Les élèves doivent alors exécuter le programme dans leur tête et en déduire la case sur laquelle l'alien s'arrêtera à la fin de l'exécution du programme.

La bibliothèque permet de générer automatiquement une correction de l'exercice :

<img src="https://user-images.githubusercontent.com/53106394/132256753-5725039b-a575-4d73-939d-996f8784726f.png" width="400" />

## Organisation des fichiers

- À la racine se trouve un fichier `alien.pdf` à distribuer aux élèves. Ce fichier contient la grille de déplacement de l'alien ainsi que 20 cases réponses.

- Le dossier `exercices` contient les 20 exercices de bases

  - Le dossier `sujets` contient les programmes au format image

    - La ligne d'importation ainsi que la ligne de génération d'image sont automatiquement retirées lors de la génération de l'image

  - Le dossier `corrections` contient la correction des exercices
    
    - Le fichier `0.png` contient la grille de base avec l'alien 

  - Le dossier `libs` contient la librairie de base permettant de générer les corrections

  - Le dossier `tools` contient un fichier à exécuter pour générer les énoncés des programmes au format image

- Le dossier `ressources` contient les diverses ressources nécessaires au projet (images, polices, etc.)

- Le dossier `autres` contient divers fichiers en vrac

## Création d'exercices

Pour créer un exercice, il suffit de s'insiperer d'un des exercices de base fournis.

Exécuter le fichier permettra de générer la grille de correction.

Exécuter le programme dans le dossier tool permettra de générer le programme au format image.

## Exemples d'utilisation

- En cours pour introduire petit à petit les notions, en particulier quand les élèves n'ont pas encore accès à un ordinateur

- Pour générer des questions d'évaluations, et obtenir une correction qui pourra être envoyé aux élèves

- Utilisé avec des outils comme wooclap ou moodle

## License

Alien-Python est sous license MIT.

Les images d'aliens ont été réalisées par [Kenney](https://www.kenney.nl/assets/platformer-pack-redux) et sont sous license C0.
