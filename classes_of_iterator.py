import os


class Iterator:
    def __init__(self, class_name, dataset_name):
        self.dataset_name = dataset_name
        self.class_name = class_name
        class_dir = os.path.join(dataset_name, class_name)
        if not os.path.exists(class_dir):
            raise FileNotFoundError(f"Directory '{class_dir}' does not exist.")
        self.paths = [
            os.path.join(class_dir, filename)
            for filename in os.listdir(class_dir)
        ]
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.paths):
            path = self.paths[self.index]
            self.index += 1
            return path
        else:
            raise StopIteration


if __name__ == "__main__":
    cats = Iterator('cats', 'dataset')
    dogs = Iterator('dogs', 'dataset')
    
    print(next(cats))
    print(next(dogs))
    print(next(cats))
    print(next(dogs))
    print(next(cats))
    print(next(dogs))
    print(next(cats))
    print(next(dogs))
