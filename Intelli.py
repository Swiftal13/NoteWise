import customtkinter as ctk
from datetime import date
import os

# Colours:
grey = "#505050"
darkGrey = "#1C1C1C"
orange = "#FF9500"
lightGrey = "#D4D4D2"
green = "#78f060"

# Font
Font = ("Arabic Transparent", 15)
FontBold = ("Arabic Transparent", 17, "bold")

# Folderpath for textfiles
folder_path = "NoteFiles/NoteTab"
# Theme preference
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")




class NoteWise(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window properties
        self.title("Intelli")
        self.geometry("900x500")
        self.resizable(False, False)
        self.tabList = []

        self.activeTab = None # Track the active tab
        self.tabList = []



        self.sidebar = ctk.CTkFrame(master=self, fg_color=darkGrey, width=100, height=100)
        self.sidebar.place(relx=0.0, rely=0, relwidth=0.2, relheight=1)

        self.tabScroll = ctk.CTkScrollableFrame(master=self.sidebar, corner_radius=0)
        self.tabScroll.place(relx=0.00, rely=0.15, relwidth=1, relheight=0.4)

        self.iconLabel = ctk.CTkLabel(master=self.sidebar, text="NoteWise", font=FontBold)
        self.iconLabel.pack(side="top", pady=5)

        self.tabCreate = ctk.CTkButton(master=self.sidebar, text="+", font=Font, command= lambda: self.Create("Note.txt", "New Note"), fg_color=grey,
                                    hover_color=orange, corner_radius=0, width=60, height=20)
        self.tabCreate.place(relx=0.66, rely=0.07)
        self.tabDelete = ctk.CTkButton(master=self.sidebar, text="Del", font=Font, command= lambda: self.Delete(self.activeTab), fg_color=grey,
                                    hover_color=orange, corner_radius=0, width=60, height=20)
        self.tabDelete.place(relx=0.33, rely=0.07)
        self.InfoButton = ctk.CTkButton(master=self.sidebar, text="Info", font=Font, command=self.Info, fg_color=grey,
                                       hover_color=orange, corner_radius=0, width=60, height=20)
        self.InfoButton.place(relx=0.00, rely=0.07)
        # ... (other GUI elements and setup)

        self.SaveButton = ctk.CTkButton(
            master=self.sidebar, text="Save", font=Font, command=self.SaveText, fg_color=grey,
            hover_color=orange, corner_radius=0, width=60, height=30
        )
        self.SaveButton.place(relx=0.6, rely=0.9)

        # Header bar and label
        self.HeaderBar = ctk.CTkFrame(self, fg_color = grey, border_color = grey, corner_radius = 0)
        self.HeaderBar.place(relx = 0.2, rely = 0, relwidth = 1, relheight = 0.05)
        self.HeaderBar.HeaderLabel = ctk.CTkLabel


        self.EntryFrame = ctk.CTkFrame(self, fg_color=grey, border_color=lightGrey)
        self.EntryFrame.place(relx=0.2, rely=0.05, relwidth=1, relheight=0.9)
        self.TextBox = ctk.CTkTextbox(self.EntryFrame, font=Font, corner_radius=0, fg_color=lightGrey,
                                       border_color=grey, text_color=darkGrey)
        self.TextBox.place(relx=0, rely=0, relwidth=0.8, relheight=1)



    def Create(self, Filename, name):
        try:
            with open(Filename, "x") as NewFile:
                newTab = Tab(app, "Note.txt", "New note", "", date.isoformat(date.today())) 
                self.tabList.append(newTab)
                self.tabButton = ctk.CTkButton(master=self.tabScroll, text=name, fg_color=darkGrey,
                                                    width=202, height=40, corner_radius=0, hover_color=grey,
                                                    border_width=0, border_color="#1c1c1c", command = lambda: self.ActiveTab(Filename))
                self.tabButton.pack(side="top", pady=0.2) 
                self.activeTab = Filename   
        except FileExistsError:
            print("File already exists. Choose a different name")

    def ActiveTab(self, Filename):
        try:
            with open(Filename, "r") as file:
                self.TextBox.delete(1.0, "end")  # Clear existing text
                self.TextBox.insert("1.0", file.read())
                self.activeTab = Filename
                
        except FileNotFoundError:
            print(f"File '{Filename}' not found")
    
    def Delete(self, Filename):
        self.tabList = [newTab for newTab in self.tabList if newTab.Filename != Filename]
    
    def SaveText(self):
        if self.activeTab:  # Check if an active tab exists
            text = self.TextBox.get("1.0", "end-1c")  # Get text from TextBox
            try:
                with open(self.activeTab, "w") as file:
                    file.write(text)
                    print(f"Saved text to {self.activeTab}")
            except Exception as e:
                print(f"Error while saving: {e}")
        else:
            print("No active tab selected")

    def Info(self):
        root = ctk.CTkToplevel()
        root.attributes('-topmost', True)
        root.title("NoteWise - Info")
        root.geometry("400x150")
        root.resizable(False, False)

        Title = ctk.CTkLabel(master=root, text="An AI noting App", font=FontBold)
        Title.pack(side="top")
        Description = ctk.CTkLabel(master=root, text="This was researched and developed in order to implement AI,\n"
                                                    "specifically NLP (Natural Language Processing) into your notes, \n"
                                                    "allowing intuitive abilities such as text prediction and auto correction.\n Have fun!")
        Description.pack(side="top")


    def SetupTabs(self):
        for dir, folder, files in os.walk(os.getcwd()):
            for file in files:
                if file.endswith(".txt"):
                    fileName = file.rstrip(".txt")
                    self.Tab = ctk.CTkButton(master=self.TabScroll, text=f"{fileName}", fg_color=darkGrey,
                                                command=lambda fn=fileName: app.ActiveTab(fn),
                                                width=202, height=40, corner_radius=0, hover_color=grey,
                                                border_width=0, border_color="#1c1c1c")
                    self.Tab.pack(side="top", pady=0.2)
        self.SetupTabs()




class Tab():
    def __init__(self, app, Filename, name, text, date):

        self.Filename = Filename
        self.name = name
        self.text = text
        self.date = date


        


if __name__ == "__main__":
    app = NoteWise()
    app.mainloop()


