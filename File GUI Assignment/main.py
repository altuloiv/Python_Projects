from tkinter import filedialog
from tkinter import *
import os
import time
import shutil
root = Tk()
root.title('File Manager')
root.geometry("500x500")

def chooseSource():
    src = filedialog.askdirectory()
    srcEntry.insert(0, src)


def chooseDest():
    dest = filedialog.askdirectory()
    destEntry.insert(0, dest)



def transferFiles():
    sourcePath = srcEntry.get()
    destPath = destEntry.get()
    SECONDS_IN_DAY = 24 * 60 * 60
    now = time.time()
    before = now - SECONDS_IN_DAY


    def last_mod_time(fname):
        return os.path.getmtime(fname)
    for fname in os.listdir(sourcePath):
        src_fname = os.path.join(sourcePath, fname)
        if last_mod_time(src_fname) > before:
            dst_fname = os.path.join(destPath, fname)
            shutil.move(src_fname, dst_fname)


srcEntry = Entry(root)
srcEntry.pack(pady=26)
destEntry = Entry(root)
destEntry.pack(pady=28)

srcButton = Button(root, text="Source Folder", command=chooseSource)
srcButton.pack(pady=24)
destButton = Button(root, text="Destination Folder", command=chooseDest)
destButton.pack(pady=26)
check_button = Button(root, text="File Check", command=transferFiles)
check_button.pack(pady=24)
root.mainloop()