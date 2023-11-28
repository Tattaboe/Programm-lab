import os
import csv
from typing import List


def get_full_paths(class_name: str) -> List[str]:
    full_path = os.path.abspath('dataset')
    class_path = os.path.join(full_path, class_name)
    image_names = os.listdir(class_path)
    image_full_paths = list(
        map(lambda name: os.path.join(class_path, name), image_names))
    return image_full_paths



def main() -> None:
 
 dataset_path = "dataset"
 classes = ["cats", "dogs"]

 with open("annotation_2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["full_path", "relative_path", "class"])

    for class_name in classes:
        class_path = os.path.join(dataset_path, class_name)

        for file_name in os.listdir(class_path):
           
            relative_path = os.path.join(class_name, file_name)
            writer.writerow([full_path, relative_path, class_name])

if __name__ == "__main__":
    main()