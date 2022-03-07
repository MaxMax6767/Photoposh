def FileSelect():
    from tkinter import Tk  # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()  # Stops tkinter from opening a small window
    filename = askopenfilename()  # Prompts user for file selection
    with open(filename, 'rb') as f:
        hexdata = f.read().hex()  # From Python Python 3.5 and onwards
    return hexdata
