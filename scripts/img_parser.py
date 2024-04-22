import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urls import happy, angry, surprise


def main():
    # 设置要爬取的网页 URL
    for url in surprise:
        # 发送 GET 请求并获取响应
        response = requests.get(url)

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到所有图片的标签
        image_tags = soup.find_all('img')

        # 遍历每个图片标签，获取图片 URL 并下载
        for img in image_tags:
            img_url = urljoin(url, img['src'])  # 获取图片的完整 URL
            img_name = img_url.split('/')[-1]  # 提取图片文件名
            img_path = os.path.join("../data/raw/surprise", img_name)  # 图片保存路径

            # 下载图片
            if img_name.endswith(".jpg") or img_name.endswith(".jpeg"):
                with open(img_path, 'wb') as f:
                    img_data = requests.get(img_url).content
                    f.write(img_data)
                print(f"Downloaded {img_name}")

    print("All images downloaded successfully!")


if __name__ == '__main__':
    main()