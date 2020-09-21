# from random import seed
# from random import random 
# from random import randint
# from random import randrange
# from random import choice
# import random
# import string
# import tkinter
# from tkinter import *
# from tkinter import scrolledtext
# from tkinter import messagebox
# import webbrowser
# import sqlite3

# from main import listSelection

# con=sqlite3.connect('Database/yourSavedLinksDatabase.db')
# cur=con.cursor()

# class saveYourLinks(Toplevel):
#     def __init__(self):
#         Toplevel.__init__(self)
#         self.title('Saved links')
#         self.resizable(False, False)


# ##########################################################################################################   
# # damit bestimmte ich, wo das fenster positioniert werden soll beim öffnen. Normalerweiße wird           #
# # das Fenster irgendwo oben in der Ecke positioniert, mit dem Code hier wird es genau mittig positioniert#
# # ########################################################################################################
#         w = 200 # width for the Tk root
#         h = 300 # height for the Tk root
#         # get screen width and height
#         ws = self.winfo_screenwidth() # width of the screen
#         hs = self.winfo_screenheight() # height of the screen
#         # calculate x and y coordinates for the Tk root window
#         x = (ws/2) - (w/2)
#         y = (hs/2) - (h/2)
#         # set the dimensions of the screen 
#         # and where it is placed
#         self.geometry('%dx%d+%d+%d' % (w, h, x, y))
# ###########################################################################################################

#         #top frame
#         self.top = Frame(self,height=120,)
#         self.top.pack(fill=X)
#         ##bottom frame
#         self.bottom = Frame(self,height=500)
#         self.bottom.pack(fill=X)

#         ###showLink
#         self.linkLabelDescription=Label(self.bottom, text='Your link: ')
#         self.linkLabelDescription.grid(row=0, column=0)
#         self.showLinkLabel=Label(self.bottom)
#         self.showLinkLabel.grid(row=0, column=1)