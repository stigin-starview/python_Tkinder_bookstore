from tkinter import *
from tkinter import messagebox

from h11 import Data
from backend import Database

database = Database()

window= Tk()
# window.maxsize(width=40, height=15)
window.title("Book Store")
# When a book is selected in the 
def getSelectedRow(event):
    global selectedTuple
    deleteTextBox()
    try:
        index = displayList.curselection()[0]
        selectedTuple= displayList.get(index)
        entryTitle.insert(END,selectedTuple[1])
        entryAuthor.insert(END,selectedTuple[2])
        entryYear.insert(END,selectedTuple[3])
        entryIsbn.insert(END,selectedTuple[4])
    except(IndexError):
        pass
    

def deleteTextBox():
    entryTitle.delete(0, END)
    entryAuthor.delete(0, END)
    entryYear.delete(0, END)
    entryIsbn.delete(0, END)

# Functions to retrieve information from backend.py
def dbView():
    # Delete everything in the box
    displayList.delete(0, END)
    for row in database.view():
        displayList.insert(END, row)


def dbSearch():
    displayList.delete(0, END)
    for row in database.search(entryTitle.get(), entryAuthor.get(),
                                  entryYear.get(), entryIsbn.get()):
                                  displayList.insert(END, row)
    
def dbAdd():
    displayList.delete(0, END)
    database.insert(entryTitle.get(), entryAuthor.get(),
                                  entryYear.get(), entryIsbn.get())
    displayList.insert(END, (entryTitle.get(), entryAuthor.get(),
                                  entryYear.get(), entryIsbn.get()))
    messagebox.showinfo("Sucess", "Book Added")
    
    deleteTextBox()

def dbUpdate():
    database.update(selectedTuple[0], entryTitle.get(), entryAuthor.get(),
                                  entryYear.get(), entryIsbn.get())
    messagebox.showinfo("Sucess", "Book updated")
    dbView()
    deleteTextBox()
    

def dbDelete():
    database.delete(selectedTuple[0])
    dbView()
    deleteTextBox()
    messagebox.showinfo("Sucess", "Book removed")


# Labels
labelTitle = Label(window, text="Title")
labelTitle.grid(row=0, column=0 )

labelAuthor = Label(window, text="Author")
labelAuthor.grid(row=0, column=2 )

labelYear = Label(window, text="Year")
labelYear.grid(row=1, column=0)

labelIsbn = Label(window, text="ISBN")
labelIsbn.grid(row=1, column= 2)

# Textbox
titleText = StringVar()
entryTitle = Entry(window, textvariable=titleText)
entryTitle.grid(row=0, column=1)

authorText = StringVar() 
entryAuthor = Entry(window, textvariable=authorText)
entryAuthor.grid(row=0, column=3)

yearText = StringVar()
entryYear = Entry(window, textvariable=yearText)
entryYear.grid(row=1, column=1)

isbnText = StringVar()
entryIsbn = Entry(window, textvariable=isbnText)
entryIsbn.grid(row=1, column=3)

# List box
displayList= Listbox(window, height= 10, width=50)
displayList.grid(row=2, column=0, rowspan=8, columnspan=2)

# To display the slected items in there text boxes
displayList.bind('<<ListboxSelect>>', getSelectedRow )



# Scroll bar for the list
scrollList = Scrollbar(window)
scrollList.grid(row=2, column=2, rowspan=8)
# Connecting scollbar and list
displayList.configure(yscrollcommand=scrollList.set)
scrollList.configure(command=displayList.yview)

# Adding Buttons
buttonViewAll = Button(window, text="View all", width=12, command=dbView)
buttonViewAll.grid(row=2, column=3)

buttonSearch = Button(window, text="Search entry", width=12, command=dbSearch)
buttonSearch.grid(row=3, column=3)

buttonAddEntry = Button(window, text="Add entry", width=12, command=dbAdd)
buttonAddEntry.grid(row=4, column=3)

buttonUpdate = Button(window, text="Update", width=12, command= dbUpdate)
buttonUpdate.grid(row=5, column=3)

buttonDelete = Button(window, text="Delete", width=12, command= dbDelete)
buttonDelete.grid(row=6, column=3)

buttonClose = Button(window, text="Close", width=12, command=window.destroy)
buttonClose.grid(row=7, column=3)


window.mainloop()


