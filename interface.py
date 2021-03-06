from tkinter import *
import tkinter.ttk
from tkinter import filedialog
import zipfile
import os
import glob
import pandas as pd

#THEME_COLOR = "#375362"
THEME_COLOR = "#444953"

class FolderInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("unzipper")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.opened_dir = None
        self.zip_files = None

        self.folder_name_label = Label(text="Select Folder:", bg=THEME_COLOR, fg="White")
        self.folder_name_label.grid(row=0, column=1)
        
        #Open button
        self.open_btn_image = PhotoImage(file="images/button.png")
        self.openDir_btn = Button(bg=THEME_COLOR, image=self.open_btn_image, bd=0, highlightbackground=THEME_COLOR, highlightthickness=0, command=self.openDirectory)
        self.openDir_btn.grid(row=1,column=1)

        #Middle Text
        self.central_canvas = Canvas(width=300, height=250, highlightthickness=0, bg="White")
        self.central_text = self.central_canvas.create_text(150,75, width=280, text="", fill="#000000", font=("Arial", 20, "italic"))
        self.central_canvas.grid(row=2, column=0, columnspan=3, pady=50)

        self.progress = tkinter.ttk.Progressbar(self.window, orient=HORIZONTAL,
              length = 100, mode = 'determinate')
        self.progress.grid(row=3, column=1, pady=10)


        #first button
        self.cook_btn = Button(self.window, text="Cook", fg="Black", highlightthickness=0, highlightbackground=THEME_COLOR, command=self.bar)
        self.cook_btn.grid(row=4,column=1)
        
        
        #unzip button
        self.unzip_btn_image = PhotoImage(file="images/button_unzip.png")
        self.unzip_btn = Button(image=self.unzip_btn_image, bd=0, highlightthickness=0, bg=THEME_COLOR, command=self.unzipAll)
        self.unzip_btn.grid(row=5,column=1)

        #CSV button layout temp
        self.csv_btn_image = PhotoImage(file="images/csv_button.png")
        self.csv_btn = Button(image=self.csv_btn_image, bd=0, highlightthickness=0, bg=THEME_COLOR, command=self.exportCsv)
        self.csv_btn.grid(row=6, column=1)


        #Dele button tmp 
        self.delete_btn_image = PhotoImage(file="images/delete_button.png")
        self.delete_btn = Button(image=self.delete_btn_image, bd=0, highlightthickness=0, bg=THEME_COLOR, command=self.deleteZipFiles)
        self.delete_btn.grid(row=7, column=1)

        self.window.mainloop()
    
    def openDirectory(self):
        #temp list to catch lenght
        self.opened_dir = filedialog.askdirectory()
        self.zip_files = [file for file in os.listdir(self.opened_dir) if file.endswith(".zip")]
        self.central_canvas.itemconfig(self.central_text, text=f"{len(self.zip_files)} zip files found in: {self.opened_dir}")

    
    def unzipAll(self):
        #zipfiles = [file for file in os.listdir(self.opened_dir) if file.endswith(".zip")]
        for zipf in self.zip_files:
            with zipfile.ZipFile(self.opened_dir + "/" + zipf, 'r') as zip_ref:
                zip_ref.extractall(self.opened_dir)
            print(f"Done extracting {zipf}")
        print("All done!")

    def deleteZipFiles(self):
        #zipfiles = [file for file in os.listdir(self.open_folder) if file.endswith(".zip")]
        for zfile in self.zip_files:
            os.remove(self.opened_dir + "/" + zfile)
            print(f"File {zfile} deleted!")

    def exportCsv(self):
        dirpath = self.opened_dir
        fbx_files = []
        for x in os.walk(dirpath):
            for y in glob.glob(os.path.join(x[0], "*.fbx")):
                fbx_files.append(y)
        
        files = fbx_files

        h = {"fbx_files" : files}

        df = pd.DataFrame(h)
        df.to_csv("test_csv.csv")

        data = pd.read_csv("test_csv.csv")
        print(data)
            



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
