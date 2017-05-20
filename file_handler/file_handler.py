import os


class FileHandler:
    def __init__(self, path):
        self.path = path

    def get(self):
        with open(self.path) as data_file:
            data = data_file.read()
        return data

    def set(self, data):
        with open(self.path) as data_file:
            data_file.write(data)

    def delete(self):
        confirm = str(raw_input('You are about to remove {0} are you sure?'.format(self.path)))
        if confirm == 'y' or confirm == 'yes':
            os.remove(self.path)

    def __str__(self):
        return str(self.path)
