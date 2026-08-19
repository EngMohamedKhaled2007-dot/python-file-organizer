from pathlib import Path
import csv

class Organizer:
    @staticmethod
    def get_folders_names_and_extensions():
        with open('path.csv') as file:
            folders = []
            reader = csv.DictReader(file ,fieldnames=['name', 'extension'])
            for line in reader:
                folders.append(line)
        return folders

    @staticmethod
    def create_folders(folders_names:list):
        for folder in folders_names:
            current_path = Path(f'./{folder['name']}')
            current_path.mkdir(exist_ok=True) 

    @staticmethod
    def change_dir(extensions:dict):
        current_path = Path('./')
        for file in current_path.iterdir():
            if file.suffix in extensions and file.is_file():
                file.rename(f'./{extensions[file.suffix]}/{file.name}')

    @staticmethod
    def extensions(folders_names:list):
        dict_extensions = {}
        for folder in folders_names:
            dict_extensions.update({folder['extension']:folder['name']})
        return dict_extensions