from tkinter import Label
from tkinter import *

window= Tk()
# window.maxsize(width=40, height=15)

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
displayList = Listbox(window, height= 10, width=50)
displayList.grid(row=2, column=0, rowspan=8, columnspan=2)

# Scroll bar for the list
scrollList = Scrollbar(window)
scrollList.grid(row=2, column=2, rowspan=8)
# Connecting scollbar and list
displayList.configure(yscrollcommand=scrollList.set)
scrollList.configure(command=displayList.yview)

# Adding Buttons
buttonViewAll = Button(window, text="View all", width=12)
buttonViewAll.grid(row=2, column=3)

buttonSearch = Button(window, text="Search entry", width=12)
buttonSearch.grid(row=3, column=3)

buttonAddEntry = Button(window, text="Add entry", width=12)
buttonAddEntry.grid(row=4, column=3)

buttonUpdate = Button(window, text="Update", width=12)
buttonUpdate.grid(row=5, column=3)

buttonDelete = Button(window, text="Delete", width=12)
buttonDelete.grid(row=6, column=3)

buttonClose = Button(window, text="Close", width=12)
buttonClose.grid(row=7, column=3)

window.mainloop()


