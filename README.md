# outils-de-traitement-de-corpus


## Tâche

Mon objectif est de détecter les émotions humaines, ce qui relève de la reconnaissance faciale dans la reconnaissance d'images. À travers les images faciales, chaque image présente une expression assez évidente, et l'objectif est de prédire les émotions humaines par le biais de l'entraînement.

## Corpus

J'ai trouvé un projet similaire sur Kaggle, qui dispose d'un ensemble de données d'entraînement assez volumineux. J'ai choisi https://www.kaggle.com/datasets/sujaykapadnis/emotion-recognition-dataset/data . Par conséquent, j'ai l'intention de créer un ensemble de données un peu plus petit, d'environ 4000 entrées. Chaque entrée contiendra une photo faciale ainsi que l'émotion correspondante exprimée par le visage de la personne sur la photo, qui servira de balise.

## Type de prédiction peut servir ce corpus

Reconnaissance d'émotions faciales, une forme de reconnaissance d'images.

## à quel modèle il a servi

Certains modèles spécifiquement conçus pour la détection d'objets, tels que Faster R-CNN, YOLO (You Only Look Once), SSD (Single Shot MultiBox Detector), RetinaNet, etc., peuvent être adaptés pour détecter les visages. Plus spécifiquement on peut utiliser le modèle CascadeClassifier de cv2.



