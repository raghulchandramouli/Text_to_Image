import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
from authToken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

#CREATE THE APP:

app = tk.Tk()
app.geometry("532x622")
app.title("PixelFlow")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(app, height=40, width=512)
prompt.configure(font=("Arial", 20))
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)

button = ctk.CTkButton(app, height=40, width=120)
button.configure(font=("Arial", 20), text_color="white", fg_color="blue")
button.configure(text = "Generate")
button.place(x=10, y=60)

modellid = "CompVis/stable-diffusion-v1-4"
device = "cpu"

pipe = StableDiffusionPipeline.from_pretrained(modellid, revision="fp16", torch_dtypes = torch.float16, use_auth_token=auth_token)
pipe.to(device)

def generator():
    with autocast(device):
        image = pipe(prompt.get(), guidance_scale = 0.5 )["sample"][0]

    img = ImageTk.PhotoImage(image)
    img.save('generatedImage.png')
    lmain.configure(image = img)

app.mainloop()