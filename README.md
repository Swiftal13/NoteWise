App to type up notes. On a tab
You can open new tabs to write on.
When you close it and open it again, the tabs are all still there. You can interchange between each tab.
Scroll through tabs. Anymore is saved in a folder.
The app strucures tabs in order of date modified


Next thing is to then integarte natural language processing
It can predict and autofill your sentences., and apuncutauation.
It only predicts if the text was typed. If there is a part which AI genereated, it does not predict any further till the person writes again ontop of it.
![image](https://github.com/Swiftal13/NoteWise/assets/76588047/2d8c05ca-82a2-4115-89eb-4ed370268b2d)

add widgets to create as new objects for each new note
Colour scheme modern pallete. **Might change to vibrant blue**
add highlighting mechanism


update, i switched to customtkinter module
i noticed to use the master root for the tkinter frame, i must assign the parent class of the tab object as self.frame so it exists for the object
I want to create the tabs functionality,and deletion. Then we focus on NLP processing and generation

errror with inheritance and nested loops. fixed
going to follow apple cualtor color scheme



![image](https://github.com/Swiftal13/NoteWise/assets/76588047/8c3d0fd6-51ed-46e7-8633-e0a8d074e1b1)


next thing fix button space under the + button
thencolor  hoverof tabs. i then have to create fetch and load mechanism for tabs and typbg
i could document this as practice for NEA
i have to ensure this is concise aefficnet code. No unneccesary
web app? 


![image](https://github.com/Swiftal13/NoteWise/assets/76588047/93adaa98-fe5b-45cb-9d90-c45069009ce3)
I can create tabs and scroll.

Delete tabs - only deletes one tab and thats it??? 



after this ill work on the NLP process

![image](https://github.com/Swiftal13/NoteWise/assets/76588047/c250128c-f582-4951-9b5d-2328192754ce)
night before y12 starts. I must get experience of NLP ML for NEA

save functon, bug fixed where tab number goes negative
![image](https://github.com/Swiftal13/NoteWise/assets/76588047/67a2157b-e225-46d0-bce7-46c53c852959)
info button window and numbered tabs

next different tabs load diff text
```py
        def SaveText(text, tabName):
            print(tabName)
            file = open(f"{tabName}.txt", "x")
            file.write(text)
            file.close()
```
now saves text files 
now can load files aswell, and save to both

now can overwrite different text files depending onclick
glitch, once i pressed number 2, it doesent change anymore it sticks to 2

testing NLP on seperate file for now

CSV file assign variable value to varible in script
refactor addtab fucntion 
NLP learning, finish this by nomvemrber

I made it so it takes counter value from csv. Now the overwrite varialbe always have a python file for some reaosn
