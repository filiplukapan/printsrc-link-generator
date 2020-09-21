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
import main
# from main import saveYourLinks

con=sqlite3.connect('Database/yourSavedLinksDatabase.db')
cur=con.cursor()


class savedLinks(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('450x555+350+200')
        self.title('Saved links')
        self.resizable(False, False)


        def funcDeleteLink():
            selectedLink = self.savedlistBox.curselection()
            finalLink = self.savedlistBox.get(selectedLink)
            linkID = finalLink.split(". ")[0]

            delMsgBox = messagebox.askquestion("Delete link", "Do you want to delete this link from your saved links?", icon="warning")

            if delMsgBox == 'yes':
                try:
                    cur.execute("DELETE FROM 'app.links' WHERE link_id=?", (linkID,))
                    con.commit()
                    messagebox.showinfo("Success", "The link has been deleted.")

                    self.savedlistBox.delete(0, END) ##löscht die Daten aus der Liste
                    showLinksInList = cur.execute("SELECT * FROM 'app.links'").fetchall() ###erzeugt die Daten neu
                    count=0
                    for links in showLinksInList:
                        self.savedlistBox.insert(count, str(links[0])+". " + links[2] + ": " + links[1])
                        count += 1
                except:
                    messagebox.showinfo("Info", "Link has not been deleted.")


        def internetSavedLink(event):
            databaseText = event.widget.get(ACTIVE)
            weblink = databaseText.split(": ")[1]
            webbrowser.open(weblink)

        def closeWindow():
            self.destroy()


        def funcUpdateLink():
            currentLink = self.savedlistBox.curselection()
            editLink = self.savedlistBox.get(currentLink)
            linkID = editLink.split(". ")[0]
            print(linkID)
            editPage = main.saveYourLinks()


        #top frame
        self.top = Frame(self,height=120,bg='#FEC007')
        self.top.pack(fill=X)
        ##bottom frame
        self.bottom = Frame(self,height=500,bg='#795548')
        self.bottom.pack(fill=X)

        ##listbox
        self.savedlistBox = Listbox(self.bottom,width=40,height=30)
        self.savedlistBox.grid(row=0, column=0)
        self.ssb = Scrollbar(self.bottom,orient=VERTICAL)
        self.ssb.config(command=self.savedlistBox.yview)
        self.ssb.grid(row=0,column=1,sticky=N+S)
        self.savedlistBox.config(yscrollcommand=self.ssb.set)
        self.savedlistBox.bind('<Double-Button-1>', internetSavedLink)


        ##top frame title + description
        self.savedHeading = Label(self.top, text='Your links treasure', font='arial 22 bold', fg='#292929', bg='#FEC007')
        self.savedHeading.place(x=100, y=30)
        self.savedHeadingDescription = Label(self.top, text='Explore your link treasure', font='arial 7 bold', bg='#FEC007')
        self.savedHeadingDescription.place(x=170, y=70)



        # ##edit button + description
        # self.buttonEdit = Button(self.bottom, text='Edit', width=12, font='arial 12 bold', borderwidth=1, relief='solid', command=funcUpdateLink)
        # self.buttonEdit.grid(row=0,column=2, sticky=N, padx=10, pady=100)

        ##delete button + description
        self.buttonDelete = Button(self.bottom, text='Delete', width=12, font='arial 12 bold', borderwidth=1, relief='solid', command=funcDeleteLink)
        self.buttonDelete.grid(row=0,column=2, sticky=N, padx=10, pady=150)

         ##close button + description
        self.buttonDelete = Button(self.bottom, text='Close', width=12, font='arial 12 bold', borderwidth=1, command=closeWindow)
        self.buttonDelete.place(x=270,y=300)



        showLinksInList = cur.execute("SELECT * FROM 'app.links'").fetchall()
        count=0
        for links in showLinksInList:
            self.savedlistBox.insert(count, str(links[0])+". " + links[2] + ": " + links[1])
            count += 1