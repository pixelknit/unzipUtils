import os
import zipfile
import threading

DIRPATH = r"D:\OBJ\Trees\CGAxis 3D Models Collection Volume 109 - Trees XII"

class UnzipUtils:
    def __init__(self, dirpath):
        self.dirpath = dirpath

    def unzipAll(self):
        zipfiles = [file for file in os.listdir(self.dirpath) if file.endswith(".zip")]
        for zipf in zipfiles:
            with zipfile.ZipFile(self.dirpath + "\\" + zipf, 'r') as zip_ref:
                zip_ref.extractall(self.dirpath)
            print(f"Done extracting {zipf}")
        print("All done!")

    def deleteZipFiles(self):
        zipfiles = [file for file in os.listdir(self.dirpath) if file.endswith(".zip")]
        for zfile in zipfiles:
            os.remove(self.dirpath + "\\" + zfile)
            print(f"File {zfile} deleted!")


folder1 = UnzipUtils(DIRPATH)

thread1 = threading.Thread(target=folder1.unzipAll)
thread2 = threading.Thread(target=folder1.deleteZipFiles)
thread1.start()
thread1.join()
#folder1.unzipAll()

user_choice = input("all the files were unzipped, woul you like to delete the ORIGINAL zip files, YES or NO?: ")
if user_choice.lower() == "yes":
    thread2.start()
    #folder1.deleteZipFiles()
else:
    "All original zip files will stay.."




#folder1.unzipAll()
