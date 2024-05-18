import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urls import happy, angry, surprise


def main():
    for url in surprise:
        # envoyer la requête GET et recevoir une réponse
        response = requests.get(url)

        # on utilise BeautifulSoup pour analyser HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # on trouve tous les étiquettes des images
        image_tags = soup.find_all('img')

        # parcourir tous les étiuquettes des images, obtenir les urls et les télécharger
        for img in image_tags:
            img_url = urljoin(url, img['src']) 
            img_name = img_url.split('/')[-1]  
            img_path = os.path.join("../data/raw/surprise", img_name)

            # télécharger les images
            if img_name.endswith(".jpg") or img_name.endswith(".jpeg"):
                with open(img_path, 'wb') as f:
                    img_data = requests.get(img_url).content
                    f.write(img_data)
                print(f"Downloaded {img_name}")

    print("All images downloaded successfully!")


if __name__ == '__main__':
    main()