import pickle
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")


class ColorApp(ctk.CTkToplevel):
    def __init__(self, image_path ):
        super().__init__()
        # configure window
        self.title("Color Picker")
        self.geometry(f"{800}x{600}")
        self.attributes('-topmost', True)
        #loading image
        self.load_image(image_path)
        self.pixels=None
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)  
        self.entry=None      
        
        # create sidebar frame with widgets
        ##=================left side bar frame andbutton=========================##
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(8, weight=1)
        self.entry_label=ctk.CTkLabel(self.sidebar_frame,text="RGB Color Code")
        self.entry_label.grid(row=0, column=0, padx=10, pady=5,sticky="ew")
        self.entry = ctk.CTkEntry(self.sidebar_frame,width=150)
        self.entry.grid(row=0, column=1,sticky="ew")
        self.entry1_label=ctk.CTkLabel(self.sidebar_frame,text="HEX Code")
        self.entry1_label.grid(row=1, column=0, padx=10, pady=5,sticky="ew")
        self.entry1 = ctk.CTkEntry(self.sidebar_frame,width=150)
        self.entry1.grid(row=1, column=1, padx=0, pady=5,sticky="ew")
       
        self.color_display = ctk.CTkButton(self.sidebar_frame, text=" ",width=200)
        self.color_display.grid(row=3, column=0, columnspan=2,padx=10, pady=10,sticky="ew")

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=self.save_color, text="Save Color",width=200)
        self.sidebar_button_2.grid(row=4, column=0, columnspan=2,padx=10, pady=10,sticky="ew")
        self.another_image_button = ctk.CTkButton(self.sidebar_frame, command=self.imagetobe_fabricated, text="Load Another Image",width=200)
        self.another_image_button.grid(row=5, column=0, columnspan=2,padx=10, pady=10,sticky="ew")
        
    #     self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
    #     self.appearance_mode_label.grid(row=5, column=0, padx=10, pady=10,sticky="w")
    #     self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], width=200,command=self.change_appearance_mode_event)
    #     self.appearance_mode_optionemenu.grid(row=5, column=1, padx=10, pady=5,sticky="w")
    #     self.appearance_mode_optionemenu.set("Light")


    # #####===================Changing the mode Light and Dark mode=============############
    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     ctk.set_appearance_mode(new_appearance_mode)

    def imagetobe_fabricated(self):
        imagename=ctk.filedialog.askopenfilename(initialdir="/Desktop/python codes",title="open images",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg")))
        self.load_image(imagename)
    ####=============Image loading in canvas================#########
    def load_image(self,image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image,master=self)
        if self.image is None:
            print(f"Error: Unable to load image from {image_path}")
            return

        # create a scrollable frame
        self.frame = ctk.CTkFrame(self,width=self.photo.width(),height=self.photo.height())
        self.frame.grid(row=1, column=1,padx=(1, 0), pady=(1, 0), sticky="w"+"n")

        #creating scrollbar
        hsbar= tk.Scrollbar(self.frame, orient="horizontal")
        vsbar= tk.Scrollbar(self.frame, orient="vertical")

        self.canvas = ctk.CTkCanvas(self.frame,width=self.photo.width(),height=self.photo.height(),
                                    scrollregion=(0,0,self.photo.width(),self.photo.height()),
                                    xscrollcommand=hsbar.set, yscrollcommand=vsbar.set)
        

        hsbar.pack(side="bottom", fill='x')
        vsbar.pack(side="right", fill="y")

        self.canvas.pack(side="left",expand="yes",fill="both")


        hsbar.configure(command=self.canvas.xview)
        vsbar.configure(command=self.canvas.yview)
       
        # Load image onto canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        
        #button function on canvas
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        
    def on_mousewheel(self, event):
        if event.state & 0x1:
            if event.delta < 0:  
                self.canvas.xview_scroll(1 , "units")     
            else:
                self.canvas.xview_scroll(-1 , "units")
        else:
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")
    
    def from_rgb(self,rgb):
        return "#%02x%02x%02x" % rgb
 
    def on_press(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.pixels = self.image.getpixel((x, y))
        ds = self.from_rgb((self.pixels))
        color=ds
        self.entry.delete(0,ctk.END)
        self.entry.insert(0,str(self.pixels))
        #####=====Hex Code========#
        self.entry1.delete(0,ctk.END)
        self.entry1.insert(0,str(color))
        
        self.color_display.configure(hover_color=color,fg_color=color)
   
    ####===========saving color value=============##########
    def save_color(self):
        color=self.entry.get()
        return(color)
    
    def get_current_color(self):
        x=self.pixels
        return x
    



if __name__ == "__main__":
    image_path = "C:/Users/shres/OneDrive/Desktop/Office/det/OCR_training/bounding box software/IMG1.bmp"
    app = ColorApp(image_path)
    app.mainloop()




