from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
import webbrowser

import extract_color as ext

tk = Tk()
tk.title('Color Palette Extractor')
tk.geometry("500x200")

tk.update_idletasks() # Ensure window dimensions are updated
width = tk.winfo_width()
height = tk.winfo_height()
screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()
x = (screen_width - width) // 2
y = (screen_height - height) // 2
tk.geometry(f"{width}x{height}+{x}+{y}")

background_color = (255,255,255)

def browse_file(entry):
    filename = filedialog.askopenfilename(
        initialdir="/",  # Starting directory
        title="Select an Image File",
        filetypes=(("pngs", "*.png"), ("jpg, jpeg", "*.jpg *jpeg"))
    )
    if filename:
        if(entry):
            entry.delete(0, END)
            entry.insert(0, filename)
        return filename

def browse_save_file():
    filename = filedialog.asksaveasfilename(
        defaultextension=".png",
        initialdir="/",  # Starting directory
        title="Save Color Palette",
        filetypes=(("pngs", "*.png"), ("jpg, jpeg", "*.jpg *jpeg"))
    )
    if filename:
        return filename

def open_color_picker():
    color_code = colorchooser.askcolor(title="Choose color")
    # color_code will be a tuple like ((R, G, B), '#RRGGBB') or (None, None) if cancelled
    if color_code[0]:  # Check if a color was selected (not cancelled)
        global background_color
        background_color = color_code[0]

def extract_color_palette(bg_col):
    palette_file = browse_save_file()
    palette_file = str(palette_file)
    if img_path_entry.get() and palette_file:
        ext.extract(img_path_entry.get(), palette_file, 1000, bg_col, True)

img_path_label = Label(tk,text='Image Path').grid(row=0, column=0)

img_path_entry = Entry(tk, width = 40)
img_path_entry.grid(row=0,column=1)

browse_file_btn = Button(tk,text='Browse...',bg='white',fg='black',command=lambda: browse_file(img_path_entry)).grid(row=0,column=2)
color_picker_btn = Button(tk,text='Background Color',bg='white',fg='black',command=lambda: open_color_picker()).grid(row=1,column=2)

generate_btn = Button(tk,text='Extract Color Palette',bg='white',fg='black',command= lambda: extract_color_palette(background_color)).grid(row=2,column=1)


def display_dev_credits():
    credits_window = Toplevel(tk) 
    credits_window.geometry("600x150")
    credits_window.update()

    Label(credits_window,text='Developed by JungBae Park from GooCat Studio\n teamgoocat@gmail.com').grid(row=0, column=0)
    Label(credits_window,text='').grid(row=1, column=0)
    Label(credits_window,text='Reference').grid(row=2, column=0)
    Label(credits_window,text='Image Color Extraction with Python in 4 Steps by Boriharn K').grid(row=3, column=0)
    link_label = Label(credits_window, text = 'https://towardsdatascience.com/image-color-extraction-with-python-in-4-steps-8d9370d9216e',fg="blue", cursor="hand2", font=('Arial', 10, 'underline'))
    link_label.grid(row=4, column=0);
    link_label.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://towardsdatascience.com/image-color-extraction-with-python-in-4-steps-8d9370d9216e"))
    credits_window.geometry(f"{link_label.winfo_reqwidth()}x{160}+{x}+{y}")

credits_btn = Button(tk,text='Developer Credits',bg='white',fg='black',command= display_dev_credits).place(relx=0.5, rely=0.5, anchor="center")

if __name__ == "__main__":
    tk.mainloop()