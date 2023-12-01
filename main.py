#Note-Taker Application --------------------------------------------------------------------
'''
Nataly Tuong
---
A GUI Project focused on a user-friendly digital note-taking application. 
This tool will enable users, primarily students, to effortlessly create and manage convenient digital sticky notes.
I have limited the amount of sticky notes to 3 because that is the most managable way I can code this project within my own skill and knowledge set.
---
* Please run this application using Windows, the UI and functionality is off on MacOS.
* I have listed where I have learned certain tkinter functions throughout the code.

* Brainstorming Draft: https://calstatela.instructure.com/groups/121713/pages/nataly-tuong-gui-group-assignment-describe-your-project
'''
from tkinter import *

#Creating the application's window ----------------------------------------------------------
'''
I learned how to make the window not resizable with: https://stackoverflow.com/questions/21958534/how-can-i-prevent-a-window-from-being-resized-with-tkinter
I learned how to use custom colors with: https://www.tutorialspoint.com/python/tk_colors.htm
'''
window = Tk()
window.geometry("600x240")
window.resizable(0,0) #Make the application window not resizable
window.title("Note-Taker")
window.configure(bg="#121212")

#Color-Palette + Assets ----------------------------------------------------------------------
'''
Primary-Color: White
Accent: #658dff

Pencil icon by Yurlick on Freepik with: https://www.freepik.com/free-vector/writting-pencil-design_850418.htm#query=pencil&position=0&from_view=search&track=sph&uuid=68310c30-5077-422f-a58e-82c5201349e4
Pin icon by d3images on Freepik with: https://www.freepik.com/free-photo/red-drawing-pin_953446.htm#query=push%20pin%20icon&position=16&from_view=search&track=ais&uuid=9a2b7bee-8a4b-425c-96da-ead14592afe6
Wrench image by stockking on Freepik with: "https://www.freepik.com/free-photo/top-view-open-end-wrench-wooden-background_9522472.htm#page=2&query=wrench%20clipart&position=11&from_view=search&track=ais&uuid=93570992-2fe8-41b0-ad33-4d31a91d73e0
Buttons created with: https://reviewgrower.com/button-and-badge-generator/
Background gradient created with: https://medibangpaint.com/en/
I found out how to load images from a folder in the same directory as the .py file with: https://stackoverflow.com/questions/52175943/loading-an-image-from-a-folder-that-is-in-the-same-folder-as-the-program
'''
window.iconbitmap("Assets/icon.ico") #Pencil icon
backgroundImg = PhotoImage(file="Assets/background.png") #Subtle background
    #Main Frame Assets
createNoteBtnImg = PhotoImage(file="Assets/createANoteButton.png")  #Lighter shade variant of Create Note Button
createNoteBtnImg2= PhotoImage(file="Assets/createANoteButton2.png") #Darker shade variant of Create Note Button
pinBtnImage = PhotoImage(file="Assets/pinButton.png") #Lighter shade variant of the Pin Button
pinBtnImage2 = PhotoImage(file="Assets/pinButton2.png") #Darker shade variant of the Pin Button
editBtnImage = PhotoImage(file="Assets/editButton.png")
editBtnImage2 = PhotoImage(file="Assets/editButton2.png")
    #Creation Frame Assets
saveBtnImg = PhotoImage(file="Assets/saveButton.png") #Lighter shade variant of Save Buton
saveBtnImg2 = PhotoImage(file="Assets/saveButton2.png") #Darker shade variant of Save Button
entryBoxImg = PhotoImage(file="Assets/entryBox.png") #Rounded box for entry box
entryBoxRedImg = PhotoImage(file="Assets/entryBoxRed.png") #Red color variant of the rounded entry box for UI
entryBoxOrangeImg = PhotoImage(file="Assets/entryBoxOrange.png") #Orange color variant of the rounded entry box for UI
entryBoxYellowImg = PhotoImage(file="Assets/entryBoxYellow.png") #Yellow color variant of the roundedentry box for UI
entryBoxGreenImg = PhotoImage(file="Assets/entryBoxGreen.png") #Green color variant of the rounded entry box for UI
entryBoxBlueImg = PhotoImage(file="Assets/entryBoxBlue.png") #Blue color variant of the rounded entry box for UI
entryBoxPurpleImg = PhotoImage(file="Assets/entryBoxPurple.png") #Purple color variant of the rounded entry box for UI
entryBoxBlackImg = PhotoImage(file="Assets/entryBoxBlack.png") #Black color variant of the rounded entry box for UI
confirmationBtnImg = PhotoImage(file="Assets/confirmationButton.png") #Lighter shade variant of the 1st confirmation button
confirmationBtnImg2 = PhotoImage(file="Assets/confirmationButton2.png") #Darker shade variant of the 1st confirmation button
confirmationBtnImg3 = PhotoImage(file="Assets/confirmationButton3.png") #Lighter shade variant of the 2nd confirmation button
confirmationBtnImg4 = PhotoImage(file="Assets/confirmationButton4.png") #Darker shade variant of the 2nd confirmation button
confirmationBtnImg5 = PhotoImage(file="Assets/confirmationButton5.png") #Lighter shade variant of the 3rd confirmation button
confirmationBtnImg6 = PhotoImage(file="Assets/confirmationButton6.png") #Darker shade variant of the 3rd confirmation button
#Functions ----------------------------------------------------------------------------------
'''
I learned cursor events with: https://stackoverflow.com/questions/49888623/tkinter-hovering-over-button-color-change
I learned about a cget method with: https://stackoverflow.com/questions/50013449/obtaining-the-state-of-a-tkinter-entry-widget
'''
modifiedColor = "White" #Default color is "White"
currentFont = "Arial Unicode MS"

def onCreateNoteBtnEnter(event): #When the mouse cursor hovers over the button, make it a darker shade
    createNoteBtn.config(image=createNoteBtnImg2)

def onCreateNoteBtnLeave(event): #When the mouse cursor stops hovering over the button, make it a lighter shade
    createNoteBtn.config(image=createNoteBtnImg)
    

def onSaveBtnEnter(event): #When the mouse cursor hovers over the button, make it a darker shade
    saveBtn.config(image=saveBtnImg2)

def onSaveBtnLeave(event): #When the mouse cursor stops hovering over the button, make it a lighter shade
    saveBtn.config(image=saveBtnImg)

def onConfirmationBtnEnter(event): #When the mouse cursor hovers over the button, make it a darker shade
    confirmationBtn.config(image=confirmationBtnImg2)

def onConfirmationBtnLeave(event): #When the mouse cursor stops hovering over the button, make it a lighter shade
    confirmationBtn.config(image=confirmationBtnImg)

def onConfirmationBtnEnter2(event): #When the mouse cursor hovers over the button, make it a darker shade
    confirmationBtn2.config(image=confirmationBtnImg4)

def onConfirmationBtnLeave2(event): #When the mouse cursor stops hovering over the button, make it a lighter shade
    confirmationBtn2.config(image=confirmationBtnImg3)

def onConfirmationBtnEnter3(event): #When the mouse cursor hovers over the button, make it a darker shade
    confirmationBtn3.config(image=confirmationBtnImg6)

def onConfirmationBtnLeave3(event): #When the mouse cursor stops hovering over the button, make it a lighter shade
    confirmationBtn3.config(image=confirmationBtnImg5)

def onEditBtnEnter(event): #When the mouse cursor hovers over the button, make it a darker shade
    editButton.config(image=editBtnImage2)

def onEditBtnLeave(event): #When the mouse cursor stops hovering over the button, make it a lighter shade
    editButton.config(image=editBtnImage)

def onEditBtnEnter2(event): #When the mouse cursor hovers over the button, make it a darker shade
    editButton2.config(image=editBtnImage2)

def onEditBtnLeave2(event): #When the mouse cursor stops hovering over the button, make it a lighter shade
    editButton2.config(image=editBtnImage)

def onEditBtnEnter3(event): #When the mouse cursor hovers over the button, make it a darker shade
    editButton3.config(image=editBtnImage2)

def onEditBtnLeave3(event): #When the mouse cursor stops hovering over the button, make it a lighter shade
    editButton3.config(image=editBtnImage)

def editContent(): #Make the text widget in the saved note editable or read-only as toggles
    if savedNote1ContentText.cget("state") == "disabled":
         savedNote1ContentText.config(state="normal")
         savedNote1Frame.config(relief="sunken")
    else:
        savedNote1ContentText.config(state="disabled")
        savedNote1Frame.config(relief="raised")

def editContent2(): #Make the text widget in the saved note editable or read-only as toggles
    if savedNote2ContentText.cget("state") == "disabled":
         savedNote2ContentText.config(state="normal")
         savedNote2Frame.config(relief="sunken")
    else:
        savedNote2ContentText.config(state="disabled")
        savedNote2Frame.config(relief="raised")

def editContent3(): #Make the text widget in the saved note editable or read-only as toggles
    if savedNote3ContentText.cget("state") == "disabled":
         savedNote3ContentText.config(state="normal")
         savedNote3Frame.config(relief="sunken")
    else:
        savedNote3ContentText.config(state="disabled")
        savedNote3Frame.config(relief="raised")

pinned = False
def pinWindow(): #An option for the user to pin the application's window on top
    global pinned
    if not pinned:
        window.attributes("-topmost",True)
        window.update()
        pinButton.config(image=pinBtnImage2)
        pinned = True
    else:
        pinned = False
        window.attributes("-topmost",False)
        pinButton.config(image=pinBtnImage)
        window.update()

def pinWindow2(): #An option for the user to pin the application's window on top
    global pinned
    if not pinned:
        window.attributes("-topmost",True)
        window.update()
        pinButton2.config(image=pinBtnImage2)
        pinned = True
    else:
        pinned = False
        window.attributes("-topmost",False)
        pinButton2.config(image=pinBtnImage)
        window.update()

def updatePin(): #Make the pin remain pinned or unpinned depending on its status from the previous frame
    global pinned
    if not pinned:
        pinButton.config(image=pinBtnImage)
    else:
        pinButton.config(image=pinBtnImage2)

def updatePin2(): #Make the pin remain pinned or unpinned depending on its status from the previous frame
    global pinned
    if not pinned:
        pinButton2.config(image=pinBtnImage)
    else:
        pinButton2.config(image=pinBtnImage2)

def displayCreationFrame(): #Change to the Note Creation Frame when the button is clicked
    window.geometry("600x400")
    creationFrame.pack(side="top", fill="both", expand=True)
    updatePin2()
    mainFrame.pack_forget()

def enterSave(): #Change to the Main Frame when the button is clicked
    confirmationFrame.place(x=3,y=155,height=85,width=267)

'''
I learned how to grab the text from tkinter text widget with: https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget
I learned about how to make a text widget read-only with: https://stackoverflow.com/questions/3842155/is-there-a-way-to-make-the-tkinter-text-widget-read-only
'''
def saveToOne(): #Overwrites the  first note in the main frame to the note from the customization frame
    window.geometry("600x240")
    mainFrame.pack(side="top", fill="both", expand=True)
    updatePin()
    confirmationFrame.place_forget()
    creationFrame.pack_forget()

    savedNote1TitleLabel.config(text=titleEntryBox.get(),font=(currentFont,10))
    savedNote1ContentText.config(bg=modifiedColor, state="normal") #Enables the "normal" state of the text widget in order to insert text
    savedNote1ContentText.insert(INSERT, contentText.get("1.0","end-1c")) 
    savedNote1ContentText.config(font=(currentFont,10), state="disabled") #Makes the text widget not editable anymore
    savedNote1ContentFrame.config(bg=modifiedColor)
    savedNote1TitleLabel.config(bg=modifiedColor,font=(currentFont,10))
    savedNote1Frame.config(bg=modifiedColor)
    savedNote1SeparationLabel.config(bg=modifiedColor)

    if modifiedColor == "Black":
        savedNote1SeparationLabel.config(bg=modifiedColor, fg="White")
        savedNote1ContentText.config(fg="White")
        savedNote1TitleLabel.config(fg="White")
    else:
        savedNote1SeparationLabel.config(fg="Black")
        savedNote1ContentText.config(fg="Black")
        savedNote1TitleLabel.config(fg="Black")

def saveToTwo(): #A copy of the saveToOne function but for Saved Note #2
    window.geometry("600x240")
    mainFrame.pack(side="top", fill="both", expand=True)
    updatePin()
    confirmationFrame.place_forget()
    creationFrame.pack_forget()

    savedNote2TitleLabel.config(text=titleEntryBox.get(),font=(currentFont,13))
    savedNote2ContentText.config(bg=modifiedColor, state="normal")
    savedNote2ContentText.insert(INSERT, contentText.get("1.0","end-1c"))
    savedNote2ContentText.config(state="disabled")
    savedNote2ContentFrame.config(bg=modifiedColor)
    savedNote2TitleLabel.config(bg=modifiedColor,font=(currentFont,10))
    savedNote2Frame.config(bg=modifiedColor)
    savedNote2SeparationLabel.config(bg=modifiedColor)

    if modifiedColor == "Black":
        savedNote2SeparationLabel.config(bg=modifiedColor, fg="White")
        savedNote2ContentText.config(fg="White")
        savedNote2TitleLabel.config(fg="White")
    else:
        savedNote2SeparationLabel.config(fg="Black")
        savedNote2ContentText.config(fg="Black")
        savedNote2TitleLabel.config(fg="Black")

def saveToThree(): #A copy of the saveToOne function but for Saved Note #3
    window.geometry("600x240")
    mainFrame.pack(side="top", fill="both", expand=True)
    updatePin()
    confirmationFrame.place_forget()
    creationFrame.pack_forget()

    savedNote3TitleLabel.config(text=titleEntryBox.get(),font=(currentFont,10))
    savedNote3ContentText.config(bg=modifiedColor, state="normal")
    savedNote3ContentText.insert(INSERT, contentText.get("1.0","end-1c"))
    savedNote3ContentText.config(state="disabled")
    savedNote3ContentFrame.config(bg=modifiedColor)
    savedNote3TitleLabel.config(bg=modifiedColor,font=(currentFont,10))
    savedNote3Frame.config(bg=modifiedColor)
    savedNote3SeparationLabel.config(bg=modifiedColor)

    if modifiedColor == "Black":
        savedNote3SeparationLabel.config(bg=modifiedColor, fg="White")
        savedNote2ContentText.config(fg="White")
        savedNote3TitleLabel.config(fg="White")
    else:
        savedNote3SeparationLabel.config(fg="Black")
        savedNote2ContentText.config(fg="Black")
        savedNote3TitleLabel.config(fg="Black")

def setNoteColor(selectedColor): #Change the note color according to the selected color
    global modifiedColor
    modifiedColor = "White" #Uses shades less harsh than tkinter's default colors
    if selectedColor == "Red":
        modifiedColor = "#D32F2F"
        entryBoxLabel.config(image=entryBoxRedImg)
    elif selectedColor == "Orange":
        modifiedColor = "#F57C00"
        entryBoxLabel.config(image=entryBoxOrangeImg)
    elif selectedColor == "Yellow":
        modifiedColor = "#FFEB3B"
        entryBoxLabel.config(image=entryBoxYellowImg)
    elif selectedColor == "Green":
        modifiedColor = "#4CAF50"
        entryBoxLabel.config(image=entryBoxGreenImg)
    elif selectedColor == "Blue":
        modifiedColor = "#2196F3"
        entryBoxLabel.config(image=entryBoxBlueImg)
    elif selectedColor == "Purple":
        modifiedColor = "#AB47BC"
        entryBoxLabel.config(image=entryBoxPurpleImg)
    elif selectedColor == "Black":
        modifiedColor = "Black"
        entryBoxLabel.config(image=entryBoxBlackImg)
    else:
        modifiedColor = "White"
        entryBoxLabel.config(image=entryBoxImg)

    noteFrame.config(bg=modifiedColor)
    entryBoxLabel.config(bg=modifiedColor)
    titleEntryBox.config(bg=modifiedColor)
    contentFrame.config(bg=modifiedColor)
    contentText.config(bg=modifiedColor)
    if modifiedColor == "Black":
        separationLabel.config(bg=modifiedColor, fg="White")
        titleEntryBox.config(fg="White")
        contentText.config(fg="White")
    else:
        contentText.config(fg="Black")
        titleEntryBox.config(fg="Black")
        separationLabel.config(bg=modifiedColor, fg="Black")

def findNoteColor(selectedColor): #Find the color that the user wants
    setNoteColor(selectedColor)

def setFont(selectedFont): #Find the font that the user wants
    titleEntryBox.config(font=(fontChosen.get(),10))
    contentText.config(font=(fontChosen.get(),15))

    global currentFont 
    currentFont = fontChosen.get()

   
#Main Frame ---------------------------------------------------------------------------------
mainFrame = Frame(window, bg="White")
mainFrame.pack(side="top", fill="both", expand=True)
backgroundLabel = Label(mainFrame,image=backgroundImg)
backgroundLabel.place(relheight=1,relwidth=1)
accentLabel = Label(mainFrame, bg="#658dff")
accentLabel.place(x=0,y=0,relwidth=1,height=3)

pinned = False
pinButton = Button(mainFrame,
                   bg="White",
                   bd=0,
                   command=pinWindow)
pinButton.place(x=13,y=8)
updatePin()

    #Note Count Label
noteCountLabel = Label(mainFrame, 
               bg="White",
               fg="Black", 
               text="Note-Taker",
               bd=0,
               font=("Arial Rounded MT Bold",15))
noteCountLabel.place(x=35, y=10)
instructionLabel = Label(mainFrame, 
               bg="White",
               fg="#658dff", 
               bd=0,
               text="create a note with the button on the right!",
               font=("Arial Unicode MS",10))
instructionLabel.place(x=10, y=35)

    #Create a Note Button
createNoteBtn = Button(mainFrame,
                 bg="White",
                 image=createNoteBtnImg,
                 bd=0,
                 text="Create a Note",
                 fg="White",
                 font=("Arial Unicode MS",15),
                 command=displayCreationFrame)

createNoteBtn.place(x=450, y=10)
createNoteBtn.bind("<Enter>", onCreateNoteBtnEnter)
createNoteBtn.bind("<Leave>", onCreateNoteBtnLeave)

    #Saved Note 1
'''
I learned about attaching scrollbars to text widgets with: https://www.tutorialspoint.com/how-to-attach-a-vertical-scrollbar-in-tkinter-text-widget
'''
savedNote1Frame = Frame(mainFrame, bg="White", highlightbackground="Black", highlightthickness=1, relief="raised", bd=2)
savedNote1Frame.place(x=15,y=70, height=150, width=150)
savedNote1TitleLabel = Label(savedNote1Frame,
                             bg="White",
                             text="Title",
                             fg="Black",
                             font=("Arial Unicode MS", 10))
savedNote1TitleLabel.place(x=10,y=3)
savedNote1SeparationLabel = Label(savedNote1Frame,
                                  bg="White",
                                  text="----------",
                                  fg="Black")
savedNote1SeparationLabel.place(x=10,y=20)
savedNote1ContentFrame = Frame(savedNote1Frame, bg="White")
savedNote1ContentFrame.place(x=10,y=35,width=125,height=105)
savedNote1TextScrollbar = Scrollbar(savedNote1ContentFrame, orient="vertical")
savedNote1TextScrollbar.pack(side="right", fill="y")
savedNote1ContentText = Text(savedNote1ContentFrame,
                               bg="White",
                               fg="Black",
                               font=("Arial Unicode MS", 10),
                               state="disabled")
savedNote1ContentText.place(x=0,y=0,width=110,height=105)
savedNote1TextScrollbar.config(command=savedNote1ContentText.yview)

editButton = Button(savedNote1Frame,
                    bg="White",
                    image=editBtnImage,
                    bd=0,
                    command=editContent)
editButton.place(x=125,y=5)
editButton.bind("<Enter>", onEditBtnEnter)
editButton.bind("<Leave>", onEditBtnLeave)

    #Saved Note 2
savedNote2Frame = Frame(mainFrame, bg="White", highlightbackground="Black", highlightthickness=1, relief="raised", bd=2)
savedNote2Frame.place(x=185,y=70, height=150, width=150)
savedNote2TitleLabel = Label(savedNote2Frame,
                             bg="White",
                             text="Title",
                             fg="Black",
                             font=("Arial Unicode MS", 10))
savedNote2TitleLabel.place(x=10,y=3)
savedNote2SeparationLabel = Label(savedNote2Frame,
                                  bg="White",
                                  text="----------",
                                  fg="Black")
savedNote2SeparationLabel.place(x=10,y=20)
savedNote2ContentFrame = Frame(savedNote2Frame, bg="White")
savedNote2ContentFrame.place(x=10,y=35,width=125,height=105)
savedNote2TextScrollbar = Scrollbar(savedNote2ContentFrame, orient="vertical")
savedNote2TextScrollbar.pack(side="right", fill="y")
savedNote2ContentText = Text(savedNote2ContentFrame,
                               bg="White",
                               fg="Black",
                               font=("Arial Unicode MS", 10),
                               state="disabled")
savedNote2ContentText.place(x=0,y=0,width=110,height=105)
savedNote2TextScrollbar.config(command=savedNote2ContentText.yview)

editButton2 = Button(savedNote2Frame,
                    bg="White",
                    image=editBtnImage,
                    bd=0,
                    command=editContent2)
editButton2.place(x=125,y=5)
editButton2.bind("<Enter>", onEditBtnEnter2)
editButton2.bind("<Leave>", onEditBtnLeave2)

    #Saved Note 3
savedNote3Frame = Frame(mainFrame, bg="White", highlightbackground="Black", highlightthickness=1, relief="raised", bd=2)
savedNote3Frame.place(x=360,y=70, height=150, width=150)
savedNote3TitleLabel = Label(savedNote3Frame,
                             bg="White",
                             text="Title",
                             fg="Black",
                             font=("Arial Unicode MS", 10))
savedNote3TitleLabel.place(x=10,y=3)
savedNote3SeparationLabel = Label(savedNote3Frame,
                                  bg="White",
                                  text="----------",
                                  fg="Black")
savedNote3SeparationLabel.place(x=10,y=20)
savedNote3ContentFrame = Frame(savedNote3Frame, bg="White")
savedNote3ContentFrame.place(x=10,y=35,width=125,height=105)
savedNote3TextScrollbar = Scrollbar(savedNote3ContentFrame, orient="vertical")
savedNote3TextScrollbar.pack(side="right", fill="y")
savedNote3ContentText = Text(savedNote3ContentFrame,
                               bg="White",
                               fg="Black",
                               font=("Arial Unicode MS", 10),
                               state="disabled")
savedNote3ContentText.place(x=0,y=0,width=110,height=105)
savedNote3TextScrollbar.config(command=savedNote3ContentText.yview)

editButton3 = Button(savedNote3Frame,
                    bg="White",
                    image=editBtnImage,
                    bd=0,
                    command=editContent3)
editButton3.place(x=125,y=5)
editButton3.bind("<Enter>", onEditBtnEnter3)
editButton3.bind("<Leave>", onEditBtnLeave3)

#Creation Frame -------------------------------------------------------------------------------
creationFrame = Frame(window, bg="White")
backgroundLabel2 = Label(creationFrame,image=backgroundImg)
backgroundLabel2.place(relheight=1,relwidth=1)
accentLabel2 = Label(creationFrame, bg="#658dff")
accentLabel2.place(x=0,y=0,relwidth=1,height=3)

pinButton2 = Button(creationFrame,
                   bg="White",
                   bd=0,
                   command=pinWindow2)

pinButton2.place(x=13,y=8)

    #Note Frame
noteFrame = Frame(creationFrame, bg="White", highlightbackground="#658dff", highlightthickness=1)
noteFrame.place(x=25, y=60, width=250, height=300)

    #Note Title Entry Box
noteTitleLabel = Label(creationFrame,
                       bg="White",
                       fg="Black", 
                       text="Note Creation",
                       bd=0,
                       font=("Arial Rounded MT Bold",15))
noteTitleLabel.place(x=35, y=10)

instructionLabel2 = Label(creationFrame, 
               bg="White",
               fg="#658dff", 
               bd=0,
               text="text on the left, customization on the right",
               font=("Arial Unicode MS",10))
instructionLabel2.place(x=10, y=35)

entryBoxLabel = Label(noteFrame,
                      bg="White",
                      image=entryBoxImg)
entryBoxLabel.place(x=5,y=7)

titleEntryBox = Entry(noteFrame,
                      bg="White",
                      fg="Black",
                      bd=0,
                      font=("Arial Unicode MS",10),
                      width=24)
titleEntryBox.place(x=10,y=20)

separationLabel = Label(noteFrame,
                        bg="White",
                        fg="Black",
                        bd=0,
                        text="--------------------------------------------")
separationLabel.place(x=7,y=55)

    #Content Frame
contentFrame = Frame(noteFrame, bg="White")
contentFrame.place(x=10, y=85, width=225, height=200)

contentTextScrollbar = Scrollbar(contentFrame, orient="vertical")
contentTextScrollbar.pack(side="right", fill="y")
contentText = Text(noteFrame,
                   bg="White",
                   fg="Black",
                   bd=1,
                   font=("Arial Unicode MS",15),
                   yscrollcommand=contentTextScrollbar.set,
                   width=25)
contentText.place(x=10,y=85, width=210, height=200)
contentTextScrollbar.config(command=contentText.yview)

    #Customization Frame
customizationFrame = Frame(creationFrame, bg="White", highlightbackground="#658dff", highlightthickness=1)
customizationFrame.place(x=300, y=60, width=275, height=250)
instructionLabel3 = Label(customizationFrame,
                          bg="White",
                          fg="Black",
                          text="Pick a Color",
                          font=("Arial Unicode MS",10))
instructionLabel3.place(x=0,y=0)
colorOptionList = ["White","Black","Red","Orange","Yellow","Green","Blue","Purple"]
color = StringVar(customizationFrame)
color.set("White")
colorOptionMenu = OptionMenu(customizationFrame,color,*colorOptionList, command=findNoteColor)
colorOptionMenu.place(x=0,y=25)
instructionLabel4 = Label(customizationFrame,
                          bg="White",
                          fg="Black",
                          text="Pick a Font",
                          font=("Arial Unicode MS",10))
instructionLabel4.place(x=0,y=55)
fontOptionsList = ["Arial Unicode MS", "Comic Sans MS", "Times New Roman", "Courier", "Calibri"]
fontChosen = StringVar(customizationFrame)
fontChosen.set("Arial Unicode MS")
fontOptionMenu = OptionMenu(customizationFrame, fontChosen, *fontOptionsList, command=setFont)
fontOptionMenu.place(x=0,y=75)

    #Save Button
saveBtn = Button(creationFrame, 
                 image=saveBtnImg,
                 bg="White",
                 bd=0,
                 font=("Arial Unicode MS",15),
                 command=enterSave)
saveBtn.place(x=525, y=340)
saveBtn.bind("<Enter>", onSaveBtnEnter)
saveBtn.bind("<Leave>", onSaveBtnLeave)

    #Confirmation Frame
confirmationFrame = Frame(customizationFrame, bg="White", highlightbackground="#658dff", highlightthickness=1)
confirmationFrameLabel = Label(confirmationFrame,
                               bg="White",
                               text="Which note would you like to override?",
                               font=("Arial Unicode MS", 10))
confirmationFrameLabel.place(x=13,y=0)
confirmationBtn = Button(confirmationFrame,
                         bg="White",
                         image=confirmationBtnImg,
                         bd=0,
                         command=saveToOne)
confirmationBtn.place(x=50,y=25)
confirmationBtn.bind("<Enter>", onConfirmationBtnEnter)
confirmationBtn.bind("<Leave>", onConfirmationBtnLeave)

confirmationBtn2 = Button(confirmationFrame,
                         bg="White",
                         image=confirmationBtnImg3,
                         bd=0,
                         command=saveToTwo)
confirmationBtn2.place(x=100,y=25)
confirmationBtn2.bind("<Enter>", onConfirmationBtnEnter2)
confirmationBtn2.bind("<Leave>", onConfirmationBtnLeave2)

confirmationBtn3 = Button(confirmationFrame,
                         bg="White",
                         image=confirmationBtnImg5,
                         bd=0,
                         command=saveToThree)
confirmationBtn3.place(x=150,y=25)
confirmationBtn3.bind("<Enter>", onConfirmationBtnEnter3)
confirmationBtn3.bind("<Leave>", onConfirmationBtnLeave3)

window.mainloop()