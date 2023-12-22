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


ActiveSelect = None  # Define ActiveSelect as a global variable


class Tab:

    def __init__(self, Filename, name, text, date):
        self.Filename = Filename
        self.name = name
        self.text = text
        self.date = date

    def tabCreate(Filename, Tabs):
        newTab = Tab(Filename, "New note", "", date.isoformat(date.today()))
        try:
            with open(newTab.Filename, "x") as NewFile:
                Tabs.append(newTab)
                

        except FileExistsError:
            print("File already exists. Chooese a different name")
    
    def tabDelete():
        del newTab
        


class NoteWise(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title("Intelli")
        self.attributes("-fullscreen", True)
        self.resizable(False, False)

        self.tabList = []


        def ActiveTab(tabName):
            global ActiveSelect
            ActiveSelect = tabName  # Set ActiveSelect to the selected tabName

            try:
                with open(ActiveSelect, "r") as file:
                    NewText = file.read()
                    self.TextEntry.insert("1.0", NewText)
            except FileNotFoundError:
                print(f"File '{ActiveSelect}' not found")


        def SaveText(text, tabName):
            print(tabName)
            try:
                with open(f"{tabName}.txt", "w") as file:
                    file.write(text)
            except Exception as e:
                print(f"Error while saving: {e}")

        def Info():
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

        self.sidebar = ctk.CTkFrame(master=self, fg_color=darkGrey, width=100, height=100)
        self.sidebar.place(relx=0.0, rely=0, relwidth=0.2, relheight=1)

        self.TabScroll = ctk.CTkScrollableFrame(master=self.sidebar, corner_radius=0)
        self.TabScroll.place(relx=0.00, rely=0.15, relwidth=1, relheight=0.4)

        self.IconLabel = ctk.CTkLabel(master=self.sidebar, text="NoteWise", font=FontBold)
        self.IconLabel.pack(side="top", pady=5)

        self.AddTab = ctk.CTkButton(master=self.sidebar, text="+", font=Font, command= lambda: Tab.tabCreate("Note.txt", self.tabList), fg_color=grey,
                                    hover_color=orange, corner_radius=0, width=60, height=20)
        self.AddTab.place(relx=0.66, rely=0.07)
        self.DelTab = ctk.CTkButton(master=self.sidebar, text="Del", font=Font, command=Tab.tabDelete, fg_color=grey,
                                    hover_color=orange, corner_radius=0, width=60, height=20)
        self.DelTab.place(relx=0.33, rely=0.07)
        self.InfoButton = ctk.CTkButton(master=self.sidebar, text="Info", font=Font, command=Info, fg_color=grey,
                                       hover_color=orange, corner_radius=0, width=60, height=20)
        self.InfoButton.place(relx=0.00, rely=0.07)
        self.SaveButton = ctk.CTkButton(master=self.sidebar, text="Save", font=Font,
                                        command=lambda: SaveText(self.TextEntry.get("0.0", "end"), ActiveSelect),
                                        fg_color=grey, hover_color=orange, corner_radius=0, width=60, height=30)
        self.SaveButton.place(relx=0.6, rely=0.9)

        # Header bar and label
        self.HeaderBar = ctk.CTkFrame(self, fg_color = grey, border_color = grey, corner_radius = 0)
        self.HeaderBar.place(relx = 0.2, rely = 0, relwidth = 1, relheight = 0.05)
        self.HeaderBar.HeaderLabel = ctk.CTkLabel


        self.EntryFrame = ctk.CTkFrame(self, fg_color=grey, border_color=lightGrey)
        self.EntryFrame.place(relx=0.2, rely=0.05, relwidth=1, relheight=0.9)
        self.TextEntry = ctk.CTkTextbox(self.EntryFrame, font=Font, corner_radius=0, fg_color=lightGrey,
                                       border_color=grey, text_color=darkGrey)
        self.TextEntry.place(relx=0, rely=0, relwidth=0.8, relheight=1)

        def SetupTabs():
            for dir, folder, files in os.walk(os.getcwd()):
                for file in files:
                    if file.endswith(".txt"):
                        fileName = file.rstrip(".txt")
                        self.AddTab = ctk.CTkButton(master=self.TabScroll, text=f"{fileName}", fg_color=darkGrey,
                                                   command=lambda fn=fileName: ActiveTab(fn),
                                                   width=202, height=40, corner_radius=0, hover_color=grey,
                                                   border_width=0, border_color="#1c1c1c")
                        self.AddTab.pack(side="top", pady=0.2)
        SetupTabs()

if __name__ == "__main__":
    app = NoteWise()
    app.mainloop()
