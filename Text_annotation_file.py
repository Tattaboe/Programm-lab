import os
import csv
from typing import List


def get_full_paths(class_name: str) -> List[str]:
    """
    Возвращает список абсолютных путей для изображений

    Данная функция возвращает список абсолютных путей для всех изображений определенного
    класса, переданного в функцию
    Parameters
    ----------
    class_name : str
      Имя класса
    Returns
    -------
    list
    Список абсолютных путей к изображениям
    """
    full_path = os.path.abspath('dataset')
    class_path = os.path.join(full_path, class_name)
    image_names = os.listdir(class_path)
    image_full_paths = list(
        map(lambda name: os.path.join(class_path, name), image_names))
    return image_full_paths


def creating_annotation():
    dataset_path = "dataset"
    classes = ["cats", "dogs"]

    with open("annotation.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["full_path", "relative_path", "class"])

        for class_name in classes:
            class_path = os.path.join(dataset_path, class_name)
            full_paths = get_full_paths(class_name)

            for full_path in full_paths:
                relative_path = os.path.relpath(full_path, dataset_path)
                writer.writerow([full_path, relative_path, class_name])


if __name__ == "__main__":
    creating_annotation()
