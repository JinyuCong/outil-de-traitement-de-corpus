import csv
import glob



with open("./dataset.csv", "w", newline="\n", encoding='utf-8') as f:
    writer = csv.writer(f)
    for img in glob.glob("../data/cleaned/*/*.jpg"):
        if img.split("\\")[-2] == 'angry':
            label = 0
        elif img.split("\\")[-2] == 'happy':
            label = 1
        else:
            label = 2
        writer.writerow((img, label))
