from tkinter import *
from PIL import Image, ImageTk
from voice_assistant import GetAI

# Function to create a gradient background
def create_gradient(canvas, color1, color2, width, height):
    gradient = PhotoImage(width=width, height=height)
    for y in range(height):
        r = int(color1[1:3], 16) + (int(color2[1:3], 16) - int(color1[1:3], 16)) * y // height
        g = int(color1[3:5], 16) + (int(color2[3:5], 16) - int(color1[3:5], 16)) * y // height
        b = int(color1[5:7], 16) + (int(color2[5:7], 16) - int(color1[5:7], 16)) * y // height
        color = f'#{r:02x}{g:02x}{b:02x}'
        gradient.put(color, to=(0, y, width, y+1))
    canvas.create_image((width/2, height/2), image=gradient, state="normal")
    canvas.gradient = gradient  # Keep a reference to avoid garbage collection

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    if fullscreen:
        root.attributes('-fullscreen', True)
    else:
        root.attributes('-fullscreen', False)
        root.geometry('800x600')  # Default window size when not in full-screen

# Create the main application window
root = Tk()
root.title("Jarvis: Your AI assistant")
root.geometry('800x600')  # Default window size
fullscreen = False  # Start in windowed mode

# Create a canvas widget for the gradient background
width = 800
height = 600
canvas = Canvas(root, width=width, height=height)
canvas.pack(fill="both", expand=True)

# Define the gradient colors (dark blue gradient)
color1 = "#1e3c72"
color2 = "#2a5298"
create_gradient(canvas, color1, color2, width, height)

# Modern font styles
font_style = ("Helvetica", 12, "bold")

# Mic string variable
mic_string_var = StringVar()

# Chatbox
chatbox = Text(root, bg="#ededed", fg="black", font=("Helvetica", 12, "bold"),
               width=48, height=6, padx=10, pady=10, relief="flat")
chatbox.config(state=DISABLED)
chatbox.place(relx=0.5, rely=0.7, anchor='center')

# Initialize the voice assistant
chatai = GetAI(root=root, status_text_var=mic_string_var, chatbox=chatbox)

# Mic button
mic_icon_image = Image.open("mic.png")
mic_icon_photo = ImageTk.PhotoImage(mic_icon_image)
mic_button = Button(root, image=mic_icon_photo,
                    command=chatai.generateResponse, height=90, width=90,
                    borderwidth=0, relief="flat")
mic_button.place(relx=0.5, rely=0.25, anchor=CENTER)

# Status label
mic_string_var.set("Hi, click on the mic to speak")
status_label = Label(root, textvariable=mic_string_var,
                     font=("Helvetica", 18, "bold"), bg="#1e3c72", fg="white")
status_label.place(relx=0.5, rely=0.45, anchor='center')

# Fullscreen toggle button
toggle_button = Button(root, text="Toggle Fullscreen", command=toggle_fullscreen, font=font_style)
toggle_button.place(relx=0.5, rely=0.95, anchor='center')

# Execute Tkinter
root.mainloop()
