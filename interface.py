from tkinter import *
import tkinter.ttk
from tkinter import filedialog
import zipfile
import os

THEME_COLOR = "#375362"

class FolderInterface:
    def __init__(self, dirpath):
        self.window = Tk()
        self.window.title("unzipper")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.folder_name_label = Label(text="Place holder", bg=THEME_COLOR)
        self.folder_name_label.grid(row=0, column=1)

        self.central_canvas = Canvas(width=300, height=250, highlightthickness=0, bg="White")
        self.central_text = self.central_canvas.create_text(150,75, width=280, text="something", fill="#000000", font=("Arial", 20, "italic"))
        self.central_canvas.grid(row=1, column=0, columnspan=3, pady=50)

        self.progress = tkinter.ttk.Progressbar(self.window, orient=HORIZONTAL,
              length = 100, mode = 'determinate')
        self.progress.grid(row=2, column=1, pady=10)


        #first button
        self.cook_btn = Button(self.window, text="Cook", highlightthickness=0, bg=THEME_COLOR, command=self.bar)
        self.cook_btn.grid(row=3,column=1)
        
        #second button
        self.openDir_btn = Button(self.window, text="Open", command=self.openDirectory)
        self.openDir_btn.grid(row=4,column=1)


        self.window.mainloop()
    
    def openDirectory(self):
        self.open_folder = filedialog.askdirectory()
        return self.open_folder
    
    def unzipAll(self):
        zipfiles = [file for file in os.listdir(self.open_folder)if file.endswith(".zip")]
        for zipf in zipfiles:
            with zipfile.ZipFile(self.open_folder + "\\" + zipf, 'r') as zip_ref:
                zip_ref.extractall(self.open_folder)
            print(f"Done extracting {zipf}")
            break
        print("All done!")

    def deleteZipFiles(self):
        zipfiles = [file for file in os.listdir(self.open_folder) if file.endswith(".zip")]
        for zfile in zipfiles:
            os.remove(self.open_folder + "\\" + zfile)
            print(f"File {zfile} deleted!")
            break

    def bar(self):
        import time
        self.progress['value'] = 20
        self.window.update_idletasks()
        time.sleep(1)
      
        self.progress['value'] = 40
        self.window.update_idletasks()
        time.sleep(1)
      
        self.progress['value'] = 50
        self.window.update_idletasks()
        time.sleep(1)
      
        self.progress['value'] = 60
        self.window.update_idletasks()
        time.sleep(1)
      
        self.progress['value'] = 80
        self.window.update_idletasks()
        time.sleep(1)
        self.progress['value'] = 100
