from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from idlelib.tooltip import Hovertip

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
    if(palette_file == None):
        return
    palette_file = str(palette_file)
    if img_path_entry.get() and palette_file:
        ext.extract(img_path_entry.get(), palette_file, background_color, tolerance_slider.get(), limit_slider.get())

img_path_label = Label(tk,text='Image Path')
img_path_entry = Entry(tk, width = 40)
img_path_tip_msg = 'Image to extract colors from.'

browse_file_btn = Button(tk,text='Browse...',bg='white',fg='black',command=lambda: browse_file(img_path_entry))
Hovertip(img_path_label, img_path_tip_msg)
Hovertip(img_path_entry, img_path_tip_msg)

tolerance_label = Label(tk,text='Tolerance')
tolerance_slider = Scale(tk, orient = HORIZONTAL, from_ = 0, to = 100)
tolerance_slider.set(12)
tolerancee_tip_msg = 'Group colors to limit the output. 0 will not group any color and 100 will group all colors into one.'
Hovertip(tolerance_label, tolerancee_tip_msg)
Hovertip(tolerance_slider, tolerancee_tip_msg)

limit_label = Label(tk,text='limit')
limit_slider = Scale(tk, orient = HORIZONTAL, from_ = 1, to = 100)
limit_tip_msg = 'The number of extracted colors presented in the output.'
Hovertip(limit_label, limit_tip_msg)
Hovertip(limit_slider, limit_tip_msg)

color_picker_btn = Button(tk,text='Background Color',bg='white',fg='black',command=lambda: open_color_picker())
color_picker_tip_msg = 'Background color of the palette. Blank space will be filled with this color.'
Hovertip(color_picker_btn, color_picker_tip_msg)

generate_btn = Button(tk,text='Extract Color Palette',bg='white',fg='black',command= lambda: extract_color_palette(background_color))
reminder = Label(tk, text = 'Reminder: The transparent area will be considered as black!')

img_path_label.grid(row=0, column=0,)
img_path_entry.grid(row=0,column=1)
browse_file_btn.grid(row=0,column=2)

tolerance_label.grid(row = 1, column = 0)
tolerance_slider.grid(row=1, column = 1, sticky = "w")

limit_label.grid(row = 2, column = 0)
limit_slider.grid(row=2, column = 1, sticky = "w")

color_picker_btn.grid(row=2,column=1, sticky= "e")
generate_btn.grid(row=4,column=1)
reminder.grid(row = 3, column = 1)


def display_dev_credits():
    credits_window = Toplevel(tk) 
    credits_window.geometry("600x150")
    credits_window.update()

    Label(credits_window,text='Developed by JungBae Park from GooCat Studio\n teamgoocat@gmail.com').grid(row=0, column=0)
    Label(credits_window,text='').grid(row=1, column=0)
    Label(credits_window,text='Reference').grid(row=2, column=0)
    Label(credits_window,text='Image Color Extraction with Python in 4 Steps by Boriharn K').grid(row=3, column=0)
    link_label = Label(credits_window, text = 'https://towardsdatascience.com/image-color-extraction-with-python-in-4-steps-8d9370d9216e',fg="blue", cursor="hand2", font=('Arial', 10, 'underline'))
    link_label.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://towardsdatascience.com/image-color-extraction-with-python-in-4-steps-8d9370d9216e"))
    link_label.grid(row=4, column=0);
    
    credits_window.geometry(f"{link_label.winfo_reqwidth()}x{160}+{x}+{y}")

credits_label = Label(tk, text = 'Developer Credits', fg="black", cursor="hand2", font=('Arial', 10, 'underline'))
credits_label.bind("<Button-1>", lambda e: display_dev_credits())
credits_label.grid(row = 4, column=2)

if __name__ == "__main__":
    tk.mainloop()