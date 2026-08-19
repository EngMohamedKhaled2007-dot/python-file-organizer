from organizer import Organizer
dirs = Organizer.get_folders_names_and_extensions()
Organizer.create_folders(dirs)
extensions = Organizer.extensions(dirs)
Organizer.change_dir(extensions)