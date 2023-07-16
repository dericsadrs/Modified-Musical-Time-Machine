
# Attibutions 
# https://www.wallpaperflare.com/adventure-time-jake-chill-out-vibes-music-wallpaper-ybmxk/download

import tkinter as tk
from music_time_machine import BillboardPlaylistCreator
from PIL import ImageTk, Image

class MusicalTimeMachineGUI:
    def __init__(self):
        self.window = tk.Tk()

        #Create an Object upon initialization
        self.time_machine = BillboardPlaylistCreator()

        self.window.title("Deric's Musical Time Machine")
        self.window.geometry("1200x640")
        self.entry_value = None
        self.has_created_playlist = True

        self.background_image = Image.open("assets/jake_the_dog.jpg")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        
        self.create_background()
        self.create_title()
        self.create_description()
        self.create_instruction_label()
        self.create_text_field()
        
        self.window.mainloop()
        
    def create_background(self):
        background_label = tk.Label(self.window, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
    def create_title(self):
        title_label = tk.Label(self.window, text="DERIC'S MUSICAL TIME MACHINE", fg="white", bg="black", font=("Arial", 24, "bold"))
        title_label.place(x=500, y=100)
        
    def create_description(self):
        description_label = tk.Label(self.window, text="A GUI which scrapes the Billboard top 100 using BeautifulSoup, And the creates a spotfiy playlist based on the scraped data", fg="white", bg="black")
        description_label.place(x=500, y=150)
        
    def create_instruction_label(self):
        instruction_label = tk.Label(self.window, text="Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ", fg="white", bg="black")
        instruction_label.place(x=500, y=200)
        
    def create_text_field(self):
        entry = tk.Entry(self.window, width=30, font=('Arial', 12), borderwidth=2, relief='groove')
        entry.place(x=500, y=230)
        #gets the value in the tiextfield 
        entry.bind('<Return>', lambda event: self.store_entry_value(entry.get()))
        

    def store_entry_value(self, value):
        self.entry_value = value
        self.has_created_playlist = self.time_machine.create_playlist(self.entry_value) 
        self.check_and_display_congratulations(self.has_created_playlist)
        
    def check_and_display_congratulations(self, boolean_value):
        self.start_loading()
        if boolean_value:
            congratulations_text = "Congratulations! You've created a playlist"
            congratulations_label = tk.Label(self.window, text=congratulations_text, font=('Arial', 8), fg='green')
            congratulations_label.place(x=500, y=260)

        
    
# Create an instance of the GUI
gui = MusicalTimeMachineGUI()
