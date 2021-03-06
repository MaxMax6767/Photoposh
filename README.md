# Codename : Photoposh

## General Presentation :
This repo is a group project for the last year of my high school computer science group. 
The goal of this project is to allow editing of any image format by using the Bitmap format for modifications (which was imposed on us).
The use of modules is only tolerated for functionalities that are not related to image editing, so we will make ample use of them for everything that surrounds the heart of our project.

## Rules : 
-	Modules allowed if not used for image modifications
-	Image modification must not use modules

## Tools : 
- β [BMP Explanations (Detailed)](https://en.wikipedia.org/wiki/BMP_file_format)
- π οΈ [HXD (Hex Editor)](https://mh-nexus.de/en/downloads.php?product=HxD20)

## Members :
- π Matteo Houbre
- π Maxime Gug
- π MattΓ©o Metz

## Graphical User Interface (With Modules) : 
- [x] π [File Selection](https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog)
    * [Tkinter](https://docs.python.org/fr/3/library/tkinter.html) -> Easy to use, compatible and quite light. 
- [ ] π [Output & Input format selection](https://understandingdata.com/python-for-seo/converting-images-webp-python/)
    * [Pil / Pillow](https://pillow.readthedocs.io/en/stable/), Easy syntax and lots of fonctionnalities.
- [ ] π [Sliders / Buttons modifications](https://kivy.org/#home)
    * [Kivy](https://kivy.org/#home), a bit heavier than Pygame because it is based around it but syntax is easier and it has more features that we could use.
- [ ] π [Real Time image rendering](https://new.pythonforengineers.com/blog/image-and-video-processing-in-python/)
    * [OpenCV (cv2)](https://pypi.org/project/opencv-python/), offers a ton of possibilities but most importantly real time rendering. 

## Functionalities (Without Modules) :
-  [x] π Read information from BMP
-	[ ] π Brightness
-	[ ] π Contrast
-	[ ] π Saturation
-	[ ] π Crop
-	[ ] π Monochrome (B&W / Grayscale)
-	[ ] π Edge Detection
-	[ ] π Blur & Sharpness
-	[ ] π Inversion
-  [ ] π Upscale / Downscale
