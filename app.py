# Documentation consulted at:
# https://docs.python.org/3/library/os.html#files-and-directories
# https://docs.python.org/es/3/library/shutil.html
# 

import os
import shutil

class FileOrganizer:
    def __init__(self, main_path, pdfs_path, inst_path, img_path, zip_path, excel_path, torrent_path, txt_path):
        self.main_path = main_path
        self.pdfs_path = pdfs_path
        self.inst_path = inst_path
        self.img_path = img_path
        self.zip_path = zip_path
        self.excel_path = excel_path
        self.torrent_path = torrent_path
        self.txt_path = txt_path

        # Crear las carpetas si no existen
        for path in [self.pdfs_path, self.inst_path, self.img_path, self.zip_path, self.excel_path, self.torrent_path, self.txt_path]:
            if not os.path.exists(path):
                os.makedirs(path)

    def move_files(self):
        while True:
            with os.scandir(self.main_path) as entries:
                for entry in entries:
                    if entry.is_file():
                        if entry.name.endswith('.pdf'):
                            shutil.move(entry.path, self.pdfs_path)
                        elif entry.name.endswith('.exe'):
                            shutil.move(entry.path, self.inst_path)
                        elif entry.name.endswith(('.jpg', '.png', '.gif', '.jpeg', '.bmp')):
                            shutil.move(entry.path, self.img_path)
                        elif entry.name.endswith(('.zip', '.7z')):
                            shutil.move(entry.path, self.zip_path)
                        elif entry.name.endswith('.xlsx'):
                            shutil.move(entry.path, self.excel_path)
                        elif entry.name.endswith('.torrent'):
                            shutil.move(entry.path, self.torrent_path)
                        elif entry.name.endswith(('.txt', '.docx')):
                            shutil.move(entry.path, self.txt_path)
            time.sleep(10)

# Definir las rutas de las carpetas
main_path = os.path.join('C:', os.sep, 'Users', 'migue', 'Downloads')
pdfs_path = os.path.join('C:', os.sep, 'Users', 'migue', 'Downloads', 'PDFs')
inst_path = os.path.join('C:', os.sep, 'Users', 'migue', 'Downloads', 'Instaladores')
img_path = os.path.join('C:', os.sep, 'Users', 'migue', 'Downloads', 'Imagenes')
zip_path = os.path.join('C:', os.sep, 'Users', 'migue', 'Downloads', 'Zips')
excel_path = os.path.join('C:', os.sep, 'Users', 'migue', 'Downloads', 'Excels')
torrent_path = os.path.join('C:', os.sep, 'Users', 'migue', 'Downloads', 'Torrents')
txt_path = os.path.join('C:', os.sep, 'Users', 'migue', 'Downloads', 'Textos')

# Crear una instancia de la clase FileOrganizer
organizer = FileOrganizer(main_path, pdfs_path, inst_path, img_path, zip_path, excel_path, torrent_path, txt_path)

# Llamar al método move_files para comenzar a mover los archivos
organizer.move_files()