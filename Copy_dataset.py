

import os
import shutil
import csv


def get_image_paths(root_dir, class_name):
    """
    Возвращает список абсолютных и относительных путей для всех изображений определенного класса
    """
    abs_paths = []
    rel_paths = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if class_name in filename:
                abs_path = os.path.abspath(os.path.join(dirpath, filename))
                rel_path = os.path.relpath(abs_path, root_dir)
                abs_paths.append(abs_path)
                rel_paths.append(rel_path)
    return abs_paths, rel_paths


def rename_images(root_dir, class_name):
    """
    Изменяет имена изображений в директории класса, дополняя ведущими нулями
    """
    class_dir = os.path.join(root_dir, class_name)
    for i, filename in enumerate(sorted(os.listdir(class_dir))):
        old_path = os.path.join(class_dir, filename)
        new_filename = f"{class_name}_{i:04}.jpg"
        new_path = os.path.join(class_dir, new_filename)
        os.rename(old_path, new_path)


def main():
    # Определяем имена классов
    class_names = ["cats", "dogs"]

    # Удаляем существующую директорию "dataset2", если она существует.
    shutil.rmtree("dataset2", ignore_errors=True)

    # Копируем содержимое директории "dataset" в новую директорию "dataset2"
    shutil.copytree("dataset", "dataset2")

    # Заменяем имена изображений и дополняем ведущими нулями
    for class_name in class_names:
        rename_images("dataset2", class_name)

    # Создаем CSV-файл "paths2.csv" и записываем пути к изображениям
    with open("annotation2.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["abs_path", "rel_path", "class"])
        for class_name in class_names:
            abs_paths, rel_paths = get_image_paths("dataset2", class_name)
            for abs_path, rel_path in zip(abs_paths, rel_paths):
                writer.writerow([abs_path, rel_path, class_name])


if __name__ == "__main__":
    main()


