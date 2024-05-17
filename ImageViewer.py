import os
import glob

from tkinter import *
from PIL import ImageTk, Image

def resize(image, x):
    w, h = image.size
    return image.resize((x, int(h*x/w)), Image.Resampling.BILINEAR)

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.images = []
        self.image_counter = 0

        # Bilder laden
        image_path = './images'

        # Bilder laden
        for file in glob.glob(os.path.join(image_path, '*.jpg')) + glob.glob(os.path.join(image_path, '*.png')):
            i = Image.open(file)
            self.images.append(ImageTk.PhotoImage(resize(i, 400)))

        #Grid aufbauen

        self.image_label = Label(self.root, image=self.images[self.image_counter])
        self.image_label.grid(row=0, column=0, columnspan=3)

        back_button = Button(self.root, text='<<', command=lambda : self.skip(-1))
        exit_button = Button(self.root, text='Bye', command=self.root.quit)
        next_button = Button(self.root, text='>>', command=lambda : self.skip(+1))

        back_button.grid(row=1, column=0)
        exit_button.grid(row=1, column=1)
        next_button.grid(row=1, column=2)

        self.statusbar = Label(self.root, text='dummy', anchor=W, bd=1, relief=SUNKEN)
        self.statusbar.grid(row=2, column=0, columnspan=3, sticky=E + W, )

    def skip(self, number):
        if 0 <= (self.image_counter+number) < len(self.images):
            self.image_counter += number
            self.image_label.grid_forget()
            self.image_label = Label(self.root, image=self.images[self.image_counter])
            self.image_label.grid(row=0, column=0, columnspan=3)

            self.statusbar.grid_forget()
            self.statusbar = Label(self.root, text=f'Image {self.image_counter} of {len(self.images)}', anchor=W, bd=1, relief=SUNKEN)
            self.statusbar.grid(row=2, column=0, columnspan=3, sticky=E + W, )





if __name__ == '__main__':
    root = Tk()
    root.title('Image Viewer')
    root.iconbitmap('folderpictures.ico')
    root.geometry('400x350')

    iv = ImageViewer(root)

    root.mainloop()
