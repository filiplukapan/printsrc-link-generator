from random import seed
from random import random 
from random import randint
from random import randrange
from random import choice
import random
import string
import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import webbrowser
import sqlite3
import sys 

import saveLinks

con=sqlite3.connect('Database/yourSavedLinksDatabase.db')
cur=con.cursor()


class LinkGeneratorUI(object):
    def __init__(self, master):


        link = 'https://prnt.sc/'

        string.ascii_letters = 'abcdefghijklmnopqrstuvwxyz'

        self.master = master


        def logic():


            ###hole den entry wert und speichere ihn
            try:
                howMany = int(self.EntryInt.get())

                for i in range(howMany):
                    randomNr1 = str(randrange(10))
                    randomNr2 = str(randrange(10))
                    randomNr3 = str(randrange(10))
                    randomNr4 = str(randrange(10))
                    randomNr5 = str(randrange(10))
                    randomLetter1 = random.choice(string.ascii_letters)
                    randomLetter2 = random.choice(string.ascii_letters)
                    randomLetter3 = random.choice(string.ascii_letters)
                    randomLetter4 = random.choice(string.ascii_letters)
                    randomLetter5 = random.choice(string.ascii_letters)
                    randomLetter6 = random.choice(string.ascii_letters)

                    ##xx000
                    aCombi = link+randomLetter1+randomLetter2+randomNr1+randomNr2+randomNr3+randomNr4

                    ##xx0x0x
                    bCombi = link+randomLetter1+randomLetter2+randomNr1+randomLetter3+randomNr2+randomLetter4

                    ##00xxxx
                    cCombi = link+randomNr1+randomNr2+randomLetter1+randomLetter2+randomLetter3+randomLetter4

                    ##xx00xx
                    dCombi = link+randomLetter1+randomLetter2+randomNr1+randomNr2+randomLetter3+randomLetter4

                    ##xxxxxx
                    eCombi = link+randomLetter1+randomLetter2+randomLetter3+randomLetter4+randomLetter5+randomLetter6

                    ##xxx000
                    fCombi = link+randomLetter1+randomLetter2+randomLetter3+randomNr1+randomNr2+randomNr3

                    yourLinks = random.choice([aCombi, bCombi, cCombi, dCombi, eCombi, fCombi])
                    self.listBox.insert(END, yourLinks)

            except ValueError:
                messagebox.showwarning("No indication set", "Please indicate the number of links you want to create.\n\nNavigate to the 'links' entry box and enter a number.\n\nHave fun! :)")


        def internet(event):
            weblink = event.widget.get(ACTIVE)
            webbrowser.open(weblink)

        def clear():
            self.listBox.delete(0, END)

        def openSavedLinks():
            savedLinksWindow = saveLinks.savedLinks()


        def saveALink():
            try:
                global listSelection
                listSelection = self.listBox.get(self.listBox.curselection())
                saveYourLinkWindow = saveYourLinks()
                print(str(listSelection))
            except TclError:
                messagebox.showerror("No link available", "Please target a link you want to save.\nIf there is no link, you can generate links through the 'Generate' button.")



        #####Frames UI Main Window

        #top frame
        self.top = Frame(master,height=120,bg='#EFEFEF', bd='1', relief='solid')
        self.top.pack(fill=X)
        ##bottom frame
        self.bottom = Frame(master,height=500,bg='#CFC9E4')
        self.bottom.pack(fill=X)
        ##graphical title
        self.heading = Label(self.top, text='LightShot Link Generator', font='arial 22 bold', fg='#292929', bg='#EFEFEF')
        self.heading.place(x=140, y=30)
        ##title description
        self.headingDescription = Label(self.top, text='Welcome! This program generates random LightShot links. Have fun exploring!', font='arial 7 bold')
        self.headingDescription.place(x=140, y=70)

        ##top photos
        ##feather photos
        self.featherPhoto = PhotoImage(file='img/schreibenResized.png')
        self.featherPhoto_label = Label(self.top, image=self.featherPhoto, width=100, height=100)
        self.featherPhoto_label.place(x=30,y=1)

        self.featherPhoto2 = PhotoImage(file='img/schreibenResized.png')
        self.featherPhoto2_label = Label(self.top, image=self.featherPhoto, width=100, height=100)
        self.featherPhoto2_label.place(x=530,y=1)
        
        
        #bottom
        ##listbox
        self.sb = Scrollbar(self.bottom,orient=VERTICAL)
        self.listBox = Listbox(self.bottom,width=60,height=27, highlightcolor='#9D27B0', fg='black')
        self.listBox.grid(row=0, column=0, padx=(50,0))
        self.sb.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=1,sticky=N+S)
        self.listBox.bind('<Double-Button-1>', internet)

        ###bottom photos
        ##treasure
        self.treasurePhoto = PhotoImage(file='img/truheResized.png')
        self.treasurePhoto_label = Label(self.bottom, image=self.treasurePhoto, width=100, height=100, bg='#CFC9E4')
        self.treasurePhoto_label.place(x=560,y=350)

        ##coins
        self.muenzPhoto = PhotoImage(file='img/muenzenResized.png')
        self.muenzPhoto_label = Label(self.bottom, image=self.muenzPhoto, width=70, height=70, bg='#CFC9E4')
        self.muenzPhoto_label.place(x=500,y=360)
        self.muenzPhoto2_label = Label(self.bottom, image=self.muenzPhoto, width=40, height=40, bg='#CFC9E4')
        self.muenzPhoto2_label.place(x=460,y=390)

        ##pirateCoin
        self.piratecPhoto = PhotoImage(file='img/pirateCoinResized.png')
        self.piratePhoto_label = Label(self.bottom, image=self.piratecPhoto, width=50, height=70, bg='#CFC9E4')
        self.piratePhoto_label.place(x=608,y=283)

        ##arrowLeft for Coin
        self.arrowBackPhoto = PhotoImage(file='img/arrowBackResized.png')
        self.arrowBackPhoto_label = Label(self.bottom, image=self.arrowBackPhoto, width=25, height=25, bg='#CFC9E4')
        self.arrowBackPhoto_label.place(x=578,y=303)

        self.arrowSidePhoto = PhotoImage(file='img/sideArrowResized.png')
        self.arrowSidePhoto_label = Label(self.bottom, image=self.arrowSidePhoto, width=25, height=25, bg='#CFC9E4')
        self.arrowSidePhoto_label.place(x=540,y=40)

        ##bottom description
        self.bottomDescription = Label(self.bottom, text='How many links do you want to create?', font='arial 7 bold', borderwidth=1, relief='solid', width=33)
        self.bottomDescription.place(x=440, y=20)

        ##entry field + description
        self.EntryInt = Entry(self.bottom, width=5,  bd='1', relief='solid')
        self.EntryInt.place(x=440, y=50)
        self.entryDescription=Label(self.bottom, text='links.', bd='1', relief='sunken', width=7)
        self.entryDescription.place(x=480, y=50)

        ##GENERATE
        self.buttonGenerate = Button(self.bottom, text='Generate', width=12, font='arial 12 bold', borderwidth=2, relief="raised", command=logic)
        self.buttonGenerate.grid(row=0,column=2, sticky=N, padx=10, pady=80)

        ##clear button + description
        self.buttonClear = Button(self.bottom, text='Clear', width=12, font='arial 12 bold', borderwidth=2, relief="ridge", command=clear)
        self.buttonClear.grid(row=0,column=2, sticky=N, padx=10, pady=120)
        self.clearDescription = Label(self.bottom, text='Clear the list.', font='arial 7 bold', bg='#CFC9E4')
        self.clearDescription.place(x=475, y=153)

        ##save button + description
        self.buttonSave = Button(self.bottom, text='Save', width=12, font='arial 12 bold', borderwidth=1, relief='solid', command=saveALink)
        self.buttonSave.grid(row=0,column=2, sticky=N, padx=10, pady=200)
        self.saveDescription = Label(self.bottom, text='Save interesting links!', font='arial 7 bold', bg='#CFC9E4')
        self.saveDescription.place(x=455, y=233)

        ##savedLinks button + description
        self.buttonSavedLinks = Button(self.bottom, text='Saved links', width=12, font='arial 12 bold', fg='#795548', borderwidth=3, relief="solid", command=openSavedLinks)
        self.buttonSavedLinks.place(x=440, y=300)
        self.savedLinksDescription = Label (self.bottom, text='Go to your saved links', font='arial 7 bold', bg='#CFC9E4')
        self.savedLinksDescription.place(x=453, y=336)





class saveYourLinks(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title('Save link')
        self.iconbitmap('img/schreiben.ico')
        self.resizable(False, False)


        def funcSaveToDatabase():
            dblink = (str(listSelection))
            dbname = self.EntryPicName.get()
            dbdescription = self.EntryDescription.get()


            if(dblink and dbname != ''):
                query="INSERT INTO 'app.links' (link_link, link_name, link_description) VALUES (?,?,?)"
                cur.execute(query,(dblink, dbname, dbdescription))
                con.commit()
                messagebox.showinfo('Success', 'Your link was saved successfully.', icon='info')
                self.destroy()
            else:
                messagebox.showerror('Error', 'Your link was not saved.\nYou need to add at least a name to save your link.')
                self.destroy()

        ##########################################################################################################   
        # damit bestimmte ich, wo das fenster positioniert werden soll beim öffnen. Normalerweiße wird           #
        # das Fenster irgendwo oben in der Ecke positioniert, mit dem Code hier wird es genau mittig positioniert#
        # ########################################################################################################
        w = 230 # width for the Tk root
        h = 300 # height for the Tk root
        # get screen width and height
        ws = self.winfo_screenwidth() # width of the screen
        hs = self.winfo_screenheight() # height of the screen
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        ###########################################################################################################

        #top frame
        self.top = Frame(self,height=120,bg='#EFEFEF')
        self.top.pack(fill=X)
        ##bottom frame
        self.bottom = Frame(self,bg='#CFC9E4')
        self.bottom.pack(fill=X)

        ##topImage
        self.sqlPhoto = PhotoImage(file='img/sqlResized.png')
        self.sqlPhoto_label = Label(self.top, image=self.sqlPhoto, width=100, height=100, bg='#EFEFEF')
        self.sqlPhoto_label.place(x=67, y=10)

        ###showLink
        self.linkLabelDescription=Label(self.bottom, text='Link: ', bg='#CFC9E4')
        self.linkLabelDescription.grid(row=0, column=0)
        self.showLinkLabel=Label(self.bottom, text=listSelection, bg='#CFC9E4')
        self.showLinkLabel.grid(row=0, column=1)

        ##input link name
        self.picNameLabel=Label(self.bottom, text='Name: ', bg='#CFC9E4')
        self.picNameLabel.grid(row=1, column=0)
        self.EntryPicName = Entry(self.bottom, width=20,  bd='2', relief='solid')
        self.EntryPicName.grid(row=1, column=1)
        ##empty for space
        self.emptyLabel=Label(self.bottom, text='', bg='#CFC9E4')
        self.emptyLabel.grid(row=2, column=0)
        ###enter link description
        self.picDescriptionLabel=Label(self.bottom, text='Description: ', bg='#CFC9E4')
        self.picDescriptionLabel.grid(row=3, column=0)
        self.EntryDescription = Entry(self.bottom, width=20,  bd='1', relief='solid')
        self.EntryDescription.grid(row=3, column=1)

        ##empty for space
        self.emptyLabel2=Label(self.bottom, text='', bg='#CFC9E4')
        self.emptyLabel2.grid(row=4, column=0)

        ##empty for space
        self.emptyLabel3=Label(self.bottom, text='', bg='#CFC9E4')
        self.emptyLabel3.grid(row=5, column=0)

        self.saveSaveButton = Button(self.bottom, text='Save',width=15, command=funcSaveToDatabase)
        self.saveSaveButton.place(x=67, y=100)
def main():
    root = Tk()
    app = LinkGeneratorUI(root)
    root.title("LightShot Link Generator")
    root.iconbitmap('img/schreiben.ico')
    root.geometry("650x555+350+200")
    root.eval('tk::PlaceWindow . center')
    root.resizable(False,False)
    root.mainloop()

if __name__ == '__main__':
    main()