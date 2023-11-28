import os
import csv

dataset_path = "dataset"
classes = ["cats", "dogs"]

with open("annotation_1.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["full_path", "relative_path", "class"])

    for class_name in classes:
        class_path = os.path.join(dataset_path, class_name)

        for file_name in os.listdir(class_path):
            full_path = os.path.join(class_path, file_name)
            relative_path = os.path.join(class_name, file_name)
            writer.writerow([full_path, relative_path, class_name])

