# Note taking app
import customtkinter as ctk
from datetime import date
    


# Colours:
grey = "#505050"
darkGrey = "#1C1C1C"
orange = "#FF9500"
lightGrey = "#D4D4D2"


# Font
NoteFont = ("Arabic Transparent", 15)
NoteFontBold = ("Arabic Transparent", 17, "bold")

# Theme preference
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")





class NoteWise(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title("NoteWise")
        self.geometry("900x600")
        self.resizable(False, False)

        Tabs = []

        # TabCreation function
        def TabCreate():
            today = date.today()
            todayStr = date.isoformat(today)
            self.AddTab = ctk.CTkButton(master = self.TabScroll, text = "New notetab", fg_color = darkGrey, width=202, height = 40, corner_radius= 0, hover_color = grey, border_width = 0, border_color = "#1c1c1c")
            self.AddTab.pack(side = "top", pady = 0.2)
            Tabs.append(self.AddTab)
        # TabDeletion function
        def TabDelete():
            try:
                Tabs[-1].destroy()
                Tabs.remove(Tabs[-1])
            except:
                print("No tabs exist")

        # Sidebar
        self.sidebar = ctk.CTkFrame(master = self, fg_color = darkGrey, width = 100, height = 100)
        self.sidebar.place(relx=0.0, rely=0, relwidth=0.2, relheight=1)



        # Scrollable tab frame
        self.TabScroll = ctk.CTkScrollableFrame(master = self.sidebar, corner_radius = 0)
        self.TabScroll.place(relx = 0.00, rely = 0.15, relwidth = 1, relheight = 0.4)
            

        # IconLabel
        self.IconLabel = ctk.CTkLabel(master = self.sidebar, text = "NoteWise", font = NoteFontBold)
        self.IconLabel.pack(side = "top", pady = 5)

        # Menu Buttons
        self.AddTab = ctk.CTkButton(master = self.sidebar, text = "+", font = NoteFont, command = TabCreate, fg_color = grey, hover_color = orange, corner_radius = 0, width = 60, height = 20)
        self.AddTab.place(relx = 0.66, rely = 0.07)
        self.DelTab = ctk.CTkButton(master = self.sidebar, text = "Del", font = NoteFont, command = TabDelete, fg_color = grey, hover_color = orange, corner_radius = 0, width = 60, height = 20)
        self.DelTab.place(relx = 0.33, rely = 0.07)
        self.InfoButton = ctk.CTkButton(master = self.sidebar, text = "Info", font = NoteFont, command = None, fg_color = grey, hover_color = orange, corner_radius = 0, width = 60, height = 20)
        self.InfoButton.place(relx = 0.00, rely = 0.07)


        # EntryBoxFrame
        self.EntryFrame = ctk.CTkFrame(self, fg_color = grey, border_color=lightGrey)
        self.EntryFrame.place(relx = 0.2, rely = 0,  relwidth=1, relheight=1)
        self.TextEntry = ctk.CTkTextbox(self.EntryFrame,  font = NoteFont,corner_radius=0, fg_color = lightGrey, border_color=grey, text_color = darkGrey)
        self.TextEntry.place(relx = 0, rely = 0, relwidth = 0.8, relheight = 1)



if __name__ == "__main__":
    app = NoteWise()
    app.mainloop()



