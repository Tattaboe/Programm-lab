import os
import shutil
import csv
import random

def remove_directory(path):
    if os.path.isdir(path):
        shutil.rmtree(path)

def get_old_rel_path():
    return [os.path.join('dataset2', name) for name in os.listdir('dataset2')]

def get_new_rel_path():
    rand_num = random.sample(range(0, 10001), 2005)
    return [os.path.join('dataset3', f'{num}.jpg') for num in rand_num]

def dataset3():

    remove_directory('dataset3')
    os.mkdir('dataset3')
    for old_path, new_path in zip(get_old_rel_path(), get_new_rel_path()):
        shutil.copyfile(old_path, new_path)

def creating_annotation3():
    old_rel_paths = get_old_rel_path()
    new_rel_paths = get_new_rel_path()
    with open('annotation3.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')
        for old_path, new_path in zip(old_rel_paths, new_rel_paths):
            class_name = 'cats' if 'cats' in old_path else 'dogs'
            writer.writerow([os.path.abspath(new_path), os.path.relpath(new_path, 'dataset3'), class_name])


if __name__ == "__main__":
    dataset3()
    creating_annotation3()