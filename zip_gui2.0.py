# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:05:06 2019

@author: cchang
"""


import tkinter as tk
from tkinter import *
import zipfile
import os
import shutil
from tkinter import ttk


def compress_dir(dirname,zip_directory = "N",delete = "N"):


#   zip a directory directly
   
    if zip_directory == "Y":
        print("Directory name:")
        print(os.getcwd())
        print("Zipping the whole folder...")
        file_path = dirname
        os.chdir('\\'.join(dirname.split('\\')[:-1]))
        zipfilename = os.path.basename(dirname)+"_folder"
        shutil.make_archive(zipfilename, 'zip', file_path)
#        if delete == "Y":
#            print("Deleting " + dirname +" ...")
#            shutil.rmtree(dirname, ignore_errors=True)
#            print(dirname +" deleted")
       
            
        
    
#    zip a file directly
    
    elif os.path.isfile(dirname):
        print("Directory is a file, it will be zipped immediately!!")
        os.chdir('\\'.join(dirname.split('\\')[:-1]))
        file_path = dirname
        zipfilename = '_'.join(os.path.basename(dirname).split('.'))
        print('Zipping ' + zipfilename +' ...')
        zipfile.ZipFile(zipfilename + '.zip','w',zipfile.ZIP_DEFLATED).write(dirname)
        if delete == "Y":
            print("Deleting " + dirname +" ...")
            os.remove(dirname)
            print(dirname +" deleted")
        


#    zip all files under the directory
#    folders not included
        
    else:
        print("Directory name:")
        print(os.getcwd())
        print("Zipping every file inside above directory (folder not included)...")
        os.chdir(dirname)
        for file in os.listdir(dirname):
            file_path = os.path.join(dirname, file)
#            print("processing...")
#            print(file_path)
#            if zip file already then skip
            if os.path.isfile(file_path):
                if (file_path.split('.')[-1] == "zip"):
                    print(file + " is already a zip file, will be skipped!!")
                    continue
                
                else:
                    zipfilename = '_'.join(os.path.basename(file_path).split('.'))+'.zip'
                    zipfile_file = os.path.basename(file_path)
                    
                    f = zipfile.ZipFile(zipfilename, 'w',zipfile.ZIP_DEFLATED)
                    print('Zipping ' + zipfilename +' ...')
                    f.write(zipfile_file)
                    f.close()
                    if delete == "Y":
                        print("Deleting " + file +" ...")
                        os.remove(file)
                        print(file +" deleted")
            else:
                continue
    print("All tasks fininshed!")
                 

#compress_dir(dirname=r"C:\Users\sijian.xuan\Desktop\test\MARKET_DEFINITION_INTERMEDIATE3.csv",zip_directory = "N",delete="Y")



#    print("Zip finish!!")



def retrieve_input():
    input_text = zip_loc.get("1.0",END)
    input_title_cofirm.config(text=input_text.rstrip())
    print(repr(input_text.rstrip()))





root = tk.Tk()
ft = ('Calibri', 18, 'bold')
root.title('FileZipper')
input_title = Label(root, text="ZIP location", font = ft)
input_title_cofirm = Label(root, text="None", font = ft)
zip_loc= tk.Text(root, height=1, width=30)
zip_loc.insert(tk.END, "Please paste your adress here")
#adress = zip_loc.get("1.0",END)
confirm = Button(root, text="OK", command=retrieve_input, font = ft)

zip_in_folder = Label(root, text="Zip whole folder?", font = ft)
folder_zip = ttk.Combobox(root,values = ['N','Y'])

delete_after_zip = Label(root, text="Delete the file after zip?", font = ft)
folder_zip2 = ttk.Combobox(root,values = ['N','Y'])

folder_zip.current(0)
folder_zip2.current(0)
exec_zip = Button(root, text="GO!", font = ft, command=lambda : compress_dir(zip_loc.get("1.0",END).rstrip(),folder_zip.get(),folder_zip2.get()))



input_title.grid(row=0, column=0)
zip_loc.grid(row=0, column=1)
confirm.grid(row=0, column=4)
input_title_cofirm.grid(row=1, column=1)

zip_in_folder.grid(row=3, column=0)
folder_zip.grid(row=3, column=1)

delete_after_zip.grid(row=5, column=0)
folder_zip2.grid(row=5, column=1)

exec_zip.grid(row=3, column=4)
tk.mainloop()

