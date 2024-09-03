import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


root = tk.Tk()

def open_file():
    browse_text.set("Loading💀💀💀")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("PDF files", "*.pdf")])
    
    if file:
        print("File was successfully loaded")
        browse_text.set("Browse")
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            page = pdf_reader.pages[0]
            page_text = page.extract_text()
            print("First page content:")
            print(page_text)
        except Exception as e:
            print(f"An error occurred while reading the PDF: {e}")
        finally:
            file.close()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3,rowspan=3)

logo = Image.open(r'C:\Users\cason\OneDrive\Desktop\files\CODING\Py\Application.py\logo.png')
logo = ImageTk.PhotoImage(logo)


logo_label = tk.Label(image=logo)
logo_label.image = logo  
logo_label.grid(column=1, row=0)

instructions = tk.Label(root, text='Select a pdf to extract all the content')

instructions.grid(columnspan=3,column=0,row=1)

browse_text=tk.StringVar()
browse_btn=tk.Button(root, textvariable=browse_text, command=lambda:open_file(), bg="#abcdef")
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=200, height=50)
canvas.grid(columnspan=3,)
root.mainloop()