from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from fpdf import FPDF
from pathlib import Path

image_list = []

def get_list_of_images():
    global image_list
    image_list = filedialog.askopenfilenames(filetypes=[("JPG files", "*.jpg"), ("PNG files", "*.png")])

def set_listbox_contents(parent):
    file_names = []
    for file_name in image_list:
        file_name = Path(file_name).name
        file_names.append(file_name)
    file_names_var = StringVar(value=file_names)

    listbox = Listbox(parent, height=8, listvariable=file_names_var)
    listbox.grid(column=1, row=2, sticky='N, S, E, W')
    scrollbar = Scrollbar(parent)
    scrollbar.grid(column=1, row=2, sticky='N, S, E')
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

def select_images(parent):
    get_list_of_images()
    set_listbox_contents(parent)

def get_output_file_name():
    file_path = filedialog.asksaveasfilename(filetypes=[("PDF files", "*.pdf")])
    return file_path

def save_output_to_pdf(parent):
    if image_list:
        pdf = FPDF('P', 'in', 'Letter')         # P = portrait orientation, in = inches, Letter = letter size paper
        for image in image_list:
            pdf.add_page()
            pdf.image(image)
        file_path = get_output_file_name()
        if file_path:
            if file_path.endswith('.pdf') == False:
                file_path += '.pdf'
            pdf.output(file_path, "F")          # Save the PDF
            messagebox.showinfo(message='PDF created!')
            clear_image_list(parent)

def clear_image_list(parent):
    global image_list
    image_list = []
    file_names_var = StringVar(value=image_list)

    listbox = Listbox(parent, listvariable=file_names_var)
    listbox.grid(column=1, row=2, sticky='N, S, E, W')

def display_ui():
    window = tk.Tk()
    window.title('Image to PDF Converter')
    window.geometry('300x400+30+30')

    # Center contents of window
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    main_frame = tk.Frame(window)
    main_frame.grid(column=0, row=0)

    tk.Button(main_frame, text="Select Image(s)", command=lambda: select_images(main_frame)).grid(column=1, row=1, sticky='N, S, E, W')
    set_listbox_contents(main_frame)
    tk.Button(main_frame, text="Clear", command=lambda: clear_image_list(main_frame)).grid(column=1, row=3, sticky='N, S, E, W')
    tk.Button(main_frame, text="Save to PDF", command=lambda: save_output_to_pdf(main_frame)).grid(column=1, row=4, sticky='N, S, E, W')

    # Apply padding to all children of main_frame
    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    window.mainloop()

    return window

display_ui()
