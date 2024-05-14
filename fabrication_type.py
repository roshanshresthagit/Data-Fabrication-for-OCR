import tkinter as tk
from PIL import Image, ImageTk

class FabricationApp(tk.Toplevel):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("Fabrication Picker")
        self.geometry(f"{1200}x600")
        self.attributes('-topmost', True)
        # configure grid layout (2x2)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        ####+========= Load images ========###########
        original_images = [
            Image.open(r"C:\Users\shres\OneDrive\Desktop\Office\data_fabrication\Text-Fabrication\fabrication_type_1.png"),
            Image.open(r"C:\Users\shres\OneDrive\Desktop\Office\data_fabrication\Text-Fabrication\fabrication_type_2.png"),
            Image.open(r"C:\Users\shres\OneDrive\Desktop\Office\data_fabrication\Text-Fabrication\fabrication_type_3.png"),
            Image.open(r"C:\Users\shres\OneDrive\Desktop\Office\data_fabrication\Text-Fabrication\fabrication_type_4.png")
        ]

        ####==== Resize images to 400x400 ===========########
        resized_images = [img.resize((590, 400), Image.LANCZOS) for img in original_images]

        self.photo_images = [ImageTk.PhotoImage(img) for img in resized_images]

        self.buttons = []
        self.selected_index = None  
        for i, photo_image in enumerate(self.photo_images):
            button = tk.Button(self, image=photo_image)
            button.configure(command=lambda idx=i: self.change_color(idx)) 
            button.grid(row=i // 2, column=i % 2, sticky="nsew")
            self.buttons.append(button)

        self.ok_button = tk.Button(self, text="OK", command=self.ok_clicked)
        self.ok_button.grid(row=2, column=0, columnspan=2, sticky="nsew")

    def change_color(self, index):
        if self.selected_index is not None:
            self.buttons[self.selected_index].configure(bg=self.cget("bg"))
        self.buttons[index].configure(bg="green")
        self.selected_index = index  

    
    def ok_clicked(self):
        if self.selected_index is not None:
            print("fabrication image selected")
        else:
            print("No image selected")

    def get_current_index(self):
        return self.selected_index


if __name__ == "__main__":
    app = FabricationApp()
    app.mainloop()
