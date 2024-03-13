# Documentation consulted at:
# https://docs.python.org/3/library/os.html#files-and-directories
# https://docs.python.org/es/3/library/shutil.html

import os
import shutil
import time

class FileOrganizer:
    def __init__(self, main_path, folders):
        self.main_path = main_path
        self.folders = folders

        # Crear las carpetas si no existen
        for path in self.folders.values():
            if not os.path.exists(path):
                os.makedirs(path)

    def move_files(self):
        while True:
            with os.scandir(self.main_path) as entries:
                for entry in entries:
                    if entry.is_file():
                        file_ext = os.path.splitext(entry.name)[1].lower()
                        if file_ext in self.folders:
                            shutil.move(entry.path, self.folders[file_ext])
            time.sleep(10)

# Definir las rutas de las carpetas
main_path = os.path.join('C:', os.sep, 'Users', 'migue', 'Downloads')
folders = {
    '.pdf': os.path.join(main_path, 'PDFs'),
    '.exe': os.path.join(main_path, 'Instaladores'),
    '.jpg': os.path.join(main_path, 'Imagenes'),
    '.png': os.path.join(main_path, 'Imagenes'),
    '.gif': os.path.join(main_path, 'Imagenes'),
    '.jpeg': os.path.join(main_path, 'Imagenes'),
    '.bmp': os.path.join(main_path, 'Imagenes'),
    '.zip': os.path.join(main_path, 'Zips'),
    '.7z': os.path.join(main_path, 'Zips'),
    '.xlsx': os.path.join(main_path, 'Excels'),
    '.torrent': os.path.join(main_path, 'Torrents'),
    '.txt': os.path.join(main_path, 'Textos'),
    '.docx': os.path.join(main_path, 'Textos')
}

# Crear una instancia de la clase FileOrganizer
organizer = FileOrganizer(main_path, folders)

# Llamar al método move_files para comenzar a mover los archivos
organizer.move_files()
