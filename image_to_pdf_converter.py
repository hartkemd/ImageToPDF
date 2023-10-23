from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from fpdf import FPDF
from pathlib import Path
# from pillow import *
# from PIL import ImageTk, Image

def get_list_of_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("JPG files", "*.jpg"), ("PNG files", "*.png")])
    return file_paths

def set_listbox_contents(parent, image_list):
    file_names = []
    for file_name in image_list:
        file_name = Path(file_name).name
        file_names.append(file_name)
    file_names_var = StringVar(value=file_names)
    Listbox(parent, height=10, listvariable=file_names_var).grid(column=1, row=2, sticky=(N, S, E, W))

def select_images(parent):
    image_list = get_list_of_images()
    set_listbox_contents(parent, image_list)
    return image_list

def get_output_file_name():
    file_path = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def save_output_to_pdf(image_list):
    pdf = FPDF('P', 'in', 'Letter')         # P = portrait orientation, in = inches, Letter = letter size paper
    for image in image_list:
        pdf.add_page()
        pdf.image(image)
    file_path = get_output_file_name()
    if file_path:
        file_path += '.pdf'
    pdf.output(file_path, "F")              # Save the PDF
    messagebox.showinfo(message='PDF created!')

def display_ui():
    window = Tk()
    window.title('Image to PDF Converter')
    window.geometry('300x300+30+30')

    main_frame = ttk.Frame(window, padding='10', borderwidth=2, relief='solid')
    main_frame.grid(column=0, row=0)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    ttk.Button(main_frame, text="Select Image(s)", command=lambda: select_images(main_frame)).grid(column=1, row=1, sticky=(N, S, E, W))
    Listbox(main_frame).grid(column=1, row=2)
    ttk.Button(main_frame, text="Save to PDF", command=save_output_to_pdf).grid(column=1, row=3, sticky=(N, S, E, W))
    
    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    window.mainloop()

    return window

display_ui()
