
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


def dataset2():
  
    class_names = ["cats", "dogs"]

    shutil.rmtree("dataset2", ignore_errors=True)
    shutil.copytree("dataset", "dataset2")

    

    for class_name in class_names:
        rename_images("dataset2", class_name)
        
        
    for root, dirs, files in os.walk("dataset2"):
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join("dataset2", file)
            shutil.move(src_file, dst_file)

   
           
def creating_annotation2():
    with open("annotation2.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["abs_path", "rel_path", "class"])
        for class_name in class_names:
            abs_paths, rel_paths = get_image_paths("dataset2", class_name)
            for abs_path, rel_path in zip(abs_paths, rel_paths):
                writer.writerow([abs_path, rel_path, class_name])

    os.rmdir('dataset2/cats')
    os.rmdir('dataset2/dogs')
    
if __name__ == "__main__":
   dataset2()
   creating_annotation()