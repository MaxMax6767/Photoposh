# Codename : Photoposh

## General Presentation :
This repo is a group project for the last year of my high school computer science group. 
The goal of this project is to allow editing of any image format by using the Bitmap format for modifications (which was imposed on us).
The use of modules is only tolerated for functionalities that are not related to image editing, so we will make ample use of them for everything that surrounds the heart of our project.

## Rules : 
-	Modules allowed if not used for image modifications
-	Image modification must not use modules

## Tools : 
- ❓ [BMP Explanations (Detailed)](https://en.wikipedia.org/wiki/BMP_file_format)
- 🛠️ [HXD (Hex Editor)](https://mh-nexus.de/en/downloads.php?product=HxD20)

## Members :
- Matteo Houbre
- Maxime Gug
- Mattéo Metz

## Graphical User Interface (With Modules) : 
- [x] [File Selection](https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog)
    * [Tkinter](https://docs.python.org/fr/3/library/tkinter.html) -> Easy to use, compatible and quite light. 
- [x] [Output & Input format selection](https://understandingdata.com/python-for-seo/converting-images-webp-python/)
    * [Pil / Pillow](https://pillow.readthedocs.io/en/stable/), Easy syntax and lots of fonctionnalities.
- [x] [Sliders / Buttons modifications](https://kivy.org/#home)
    * [Kivy](https://kivy.org/#home), a bit heavier than Pygame because it is based around it but syntax is easier and it has more features that we could use.
- [x] [Real Time image rendering](https://new.pythonforengineers.com/blog/image-and-video-processing-in-python/)
    * [OpenCV (cv2)](https://pypi.org/project/opencv-python/), offers a ton of possibilities but most importantly real time rendering. 

## Functionalities (Without Modules) :
-  [x] Read information from BMP
-	[x] Brightness
-	[x] Contrast
-	[x] Saturation
-	[ ] Crop
-	[x] Monochrome (B&W / Grayscale)
-	[ ] Edge Detection
-	[ ] Blur & Sharpness
-	[ ] Inversion
-  [ ] Upscale / Downscale
