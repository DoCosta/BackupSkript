import tkinter as tk
from tkinter import filedialog
import shutil

window = tk.Tk()
window.title('Backup Tool')

sourcepath = ''
destpath = ''
selection = 1

def select_dir():
    global sourcepath, destpath, selection
    if selection == 1:
        folder_selected = filedialog.askdirectory()
        sourcepath = folder_selected
        lblSourcePath.config(text=sourcepath)
        btnSelectSource.config(state='disabled')
        btnSelectDestination.config(state='normal')
        selection = 2
    else:
        folder_selected = filedialog.askdirectory()
        destpath = folder_selected
        lblDestinationPath.config(text=destpath)
        btnSelectDestination.config(state='disabled')
        selection = 1

def Backup():
    global destpath
    if destpath == '':
        destpath = filedialog.askdirectory()
        lblDestinationPath.config(text=destpath)
    shutil.copytree(sourcepath, destpath, dirs_exist_ok=True)
    with open('paths.txt', 'w') as f:
        f.write(f'Source: {sourcepath}\n')
        f.write(f'Destination: {destpath}\n')

tk.Label(window, text="Select Source or Destination Path:").grid(row=0, column=2)

btnSelectSource = tk.Button(window, text="Choose Source Folder", command=select_dir)
btnSelectDestination = tk.Button(window, text="Choose Destination Folder", state='disabled', command=select_dir)
btnBackup = tk.Button(window, text="Backup", command=Backup)

lblSourcePath = tk.Label(window, text="", relief='solid', width=40)
lblDestinationPath = tk.Label(window, text="", relief='solid', width=40)

btnSelectSource.grid(row=1, column=0, padx=5, pady=5)
btnSelectDestination.grid(row=2, column=0, padx=5, pady=5)
btnBackup.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
lblSourcePath.grid(row=1, column=1, pady=5, padx=(0, 5))
lblDestinationPath.grid(row=2, column=1, pady=5, padx=(0, 5))

window.mainloop()