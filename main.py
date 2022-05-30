# Projet Photoposh : Maxime GUG | Mattéo Metz | Mattéo Houbre
# JBS 2022

# Imports
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.slider import Slider
from tkinter import Tk
from tkinter import filedialog as fd
from PIL import Image as IM
import calendar
import time

# Configuration Tkinter (Désactive l'UI Tkinter)
Tk().withdraw()

# UI
class PhotoposhApp(App):
    # Affichage
    def build(self):
        self.window = RelativeLayout()  # Def du layout de l'app (Ici, relatif à la res de l'écran)
        self.window.size_hint = (0.9, 0.9)  # Bordure de 5% de la tainne de l'écran en haut & en bas.
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}  # Gentrage de l'UI
        
        # Slider fonction luminosité + légende
        self.brightness = Slider(min=-128, max=128, value=0)  # Définition slider + Plage de fonctionnement
        self.brightness.size_hint = (0.4, 0.1)  # Définition taille (relative à la taille de la fenetre)
        self.brightness.pos_hint = {"center_x": 0.2, "center_y":0.90}  # Définition Position (relative à la taille de la fenetre)
        self.window.add_widget(self.brightness)  # Ajout du widget à l'ensemble "window" pour l'affichage
        self.brightness_text = Label(text = "Luminosité de l'image")  # Ajout légende du slider
        self.brightness_text.size_hint = (0.4, 0.1)  # Def taille légende (adaptative à la taille de l'écran)
        self.brightness_text.pos_hint = {"center_x": 0.2, "center_y":0.95}  # Def position de la légende
        self.window.add_widget(self.brightness_text)  # Ajout de la légende à l'ensemble d'affichage
        
        # Slider fonction contraste + légende
        self.contrast = Slider(min=-128, max=128, value=0)
        self.contrast.size_hint = (0.4, 0.1)
        self.contrast.pos_hint = {"center_x": 0.2, "center_y":0.80}
        self.window.add_widget(self.contrast)
        self.contrast_text = Label(text = "Contraste de l'image") 
        self.contrast_text.size_hint = (0.4, 0.1)
        self.contrast_text.pos_hint = {"center_x": 0.2, "center_y":0.85}
        self.window.add_widget(self.contrast_text)
        
        # Boutton Apply Changes
        self.applyChanges = Button(text="Apply Changes")  # Def de l'objet Boutton
        self.applyChanges.bind(on_press=self.applychanges)  # Def du callback du boutton
        self.applyChanges.pos_hint = {"center_x": 0.2, "center_y":0.65}  # Def position du boutton (relative à la taille de la fenetre)
        self.applyChanges.border = (20, 20, 20, 20)  # Arrondi des coins
        self.applyChanges.size_hint = (0.4, 0.07)  # Def taille boutton
        self.window.add_widget(self.applyChanges)  # Ajout du boutton à l'ensemble d'affichage
        
        # Boutton Nuances de gris
        self.grayscale = Button(text="Nuances de gris")
        self.grayscale.bind(on_press=self.grayscalecallback)
        self.grayscale.border = (20, 20, 20, 20)
        self.grayscale.pos_hint = {"center_x": 0.2, "center_y":0.45}
        self.grayscale.size_hint = (0.4, 0.07)
        self.window.add_widget(self.grayscale)
        
        # Boutton Inversion
        self.invert = Button(text="Inversion de couleur")
        self.invert.bind(on_press=self.inversioncallback)
        self.invert.border = (20, 20, 20, 20)
        self.invert.pos_hint = {"center_x": 0.2, "center_y":0.35}
        self.invert.size_hint = (0.4, 0.07)
        self.window.add_widget(self.invert)
        
        # Boutton FilePrompt
        self.filePrompt = Button(text="Open File")
        self.filePrompt.bind(on_press=self.fileprompt)
        self.filePrompt.border = (20, 20, 20, 20)
        self.filePrompt.pos_hint = {"center_x": 0.2, "center_y":0.15}
        self.filePrompt.size_hint = (0.4, 0.1)
        self.window.add_widget(self.filePrompt)
        
        self.cpt = 0

        return self.window
    
    
    # Méthodes de Callback
    def fileprompt(self, event):
        self.filename = fd.askopenfilename()  # Fenetre explorateur fichier par défaut : Retourne le chemin d'accès au fichier
        self.ImageData = IM.open(self.filename)  # Ouverture de fichier avec le chemin d'accès
        self.render = Image(source=self.filename)  # Création de l'objet "render" pour affichage de l'image
        self.render.size_hint = (0.5, 0.5)  # Def taille (relative à la taille de la fenetre)
        self.render.pos_hint = {"center_x": 0.75, "center_y":0.25}  # Def position (relative à la taille de la fenetre)
        self.window.add_widget(self.render)  # Ajout de l'objet render à l'affichage
        
    def applychanges(self, event):
        if self.brightness.value != 0:
            Brightness(self.ImageData, self.brightness.value)
        elif self.contrast.value != 0:
            Contrast(self.ImageData, self.contrast.value)
        
        self.cpt = calendar.timegm(time.gmtime())
        self.ImageData.save(f'{self.cpt}.png', "PNG")
        self.render = Image(source = f'{self.cpt}.png')
        self.render.size_hint = (0.5, 0.5)
        self.render.pos_hint = {"center_x": 0.75, "center_y":0.75}
        self.window.add_widget(self.render)
        
    def inversioncallback(self, event):
        Inversion(self.ImageData)
        self.cpt = calendar.timegm(time.gmtime())
        self.ImageData.save(f'{self.cpt}.png', "PNG")
        self.render = Image(source = f'{self.cpt}.png')
        self.render.size_hint = (0.5, 0.5)
        self.render.pos_hint = {"center_x": 0.75, "center_y":0.75}
        self.window.add_widget(self.render)
        
    def grayscalecallback(self, event):
        Grayscale(self.ImageData)
        self.cpt = calendar.timegm(time.gmtime())
        self.ImageData.save(f'{self.cpt}.png', "PNG")
        self.render = Image(source = f'{self.cpt}.png')
        self.render.size_hint = (0.5, 0.5)
        self.render.pos_hint = {"center_x": 0.75, "center_y":0.75}
        self.window.add_widget(self.render)
        
    def savecallback(self, event):
        self.save = fd.asksaveasfile(title="Select an Image",filetypes=[("PNG","*.png"),("JPEG","*.jpeg")])
        print(self.save)


# Fonctions édition images

def Brightness(i, v):
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            P = list(i.getpixel((x, y)))
            for w in range(3):
                P[w] += int(v)
                if P[w] < 0: 
                    P[w] = 0
                elif P[w] > 255:
                    P[w] = 255
            i.putpixel((x, y), tuple(P))
            
def Contrast(i, v):
    F = (259*(255+v))/(255*(259-v))
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            P = list(i.getpixel((x, y)))
            for w in range(3):
                P[w] = int((F * (P[w] - 128) + 128))
            i.putpixel((x, y), tuple(P))
            
def Grayscale(i):
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            P = list(i.getpixel((x, y)))
            P[0] = int(P[0] * 0.299 * + P[1] * 0.587 + P[2] * 0.114)
            P[1] = int(P[0] * 0.299 * + P[1] * 0.587 + P[2] * 0.114)
            P[2] = int(P[0] * 0.299 * + P[1] * 0.587 + P[2] * 0.114)
            i.putpixel((x, y), tuple(P))

def Inversion(i):
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            P = list(i.getpixel((x, y)))
            for w in range(3):
                P[w] = int(P[3] - P[w])
            i.putpixel((x, y), tuple(P))
    
            
if __name__ == '__main__':
    PhotoposhApp().run()
