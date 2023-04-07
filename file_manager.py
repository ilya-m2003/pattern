from tkinter import *
import os
import shutil

tk = Tk()
tk.title("Файлы и папки")
tk.geometry("240x120")
label = Label(tk, text="Введите имя папки")
label.place(x=10, y=10, width=200, height=20)
entry = Entry(tk)
entry.place(x=10, y=40, width=200, height=20)

def folder():
    entry_folder = entry.get()
    try:
        os.mkdir(entry_folder + '/Прочее')
    except FileExistsError:
        pass
    files = os.listdir(entry_folder)
    os.chdir(entry_folder)
    o = ['Д1', 'Д2', 'Д3', 'Д4']
    filenames = []
    
    for file in files:
        
        name_otdel = file.split('_')[0]
        if name_otdel in o:
            end = f"{file.split('_')[0]} + \\ + {file.split('.')[-1]}"
            try:
                os.mkdir(file.split('_')[0])
            except FileExistsError:
                pass
            
            try:
                os.mkdir(end)
            except: 
                pass
        
            try:
                shutil.move(file, end)
            except: 
                pass
        else:
            end = f"{entry_folder}\\Прочее\\{file.split('.')[-1]}"
            try:
                os.mkdir('Прочее' + '\\' + file.split('.')[-1])
            except: 
                pass
            
            try:
                shutil.move(file, end)
            except: 
                pass
        print(file, "перемещён")
            
button = Button(tk, text="Пуск", command = folder)
button.place(x=10, y=70, width=200, height=20)
tk.mainloop()
