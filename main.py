from tkinter import *
import sqlite3

def createDb():
    ''' Use just once, delete the state=DISABLED from
    createDatabase button to Enable it'''

    connection = sqlite3.connect('library.db')
    c = connection.cursor()

    c.execute('''CREATE TABLE library (
        nome_livro text,
        autor_livro text,
        fileira integer
    )''')

    connection.commit()
    connection.close()

def insertDb():
    ''' This will insert a new information in the database
    that you have created'''

    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("INSERT INTO library VALUES(:nomeEntry, :autorEntry, :fileiraEntry)", 
        {
            'nomeEntry': nomeEntry.get(),
            'autorEntry': autorEntry.get(),
            'fileiraEntry': fileiraEntry.get()

        })

    conn.commit()
    conn.close()

    nomeEntry.delete(0, END)
    autorEntry.delete(0, END)
    fileiraEntry.delete(0, END)    

def showDb():
    ''' Show the database in the library.db,
    it has some limitations of how much can show '''

    top = Toplevel()
    top.title('Books')
    top.geometry('500x500')

    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM library")
    records = c.fetchall()
    printRecord = ''

    for record in records:
        printRecord += f'Nome: {record[0]}\tAutor: {record[1]}\tFileira: {record[2]} -> oid {record[3]}\n'

    query_label = Label(top, text=printRecord)
    query_label.grid(row=0, column=0, columnspan=2)

    conn.commit()
    conn.close()

def deleteBook():
    ''' Get the oid of the book that you want to
    delete from showDb() and insert on oidSelect '''
    
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    oid_num = oidSelect.get()

    c.execute(f'DELETE from library WHERE oid={oid_num}')

    conn.commit()
    conn.close()

    oidSelect.delete(0, END)
    showDb()
    
# MAIN CODE
root = Tk()
root.title('Library Database')
root.geometry('375x400')
root.resizable(width=FALSE, height=FALSE)

# LABEL DECLARATION
nome_livroLabel = Label(root, text='Nome do livro: ')
autor_livroLabel = Label(root, text='Autor do livre: ')
fileiraLabel = Label(root, text='Fileira: ')
oidLabel = Label(root, text="Select ID: ")

# ENTRY DECLARATION
nomeEntry = Entry(root, width=40)
autorEntry = Entry(root, width=40)
fileiraEntry = Entry(root, width=40)
oidSelect = Entry(root, width=20)

# BUTTON DECLARATION
insertIntoDb = Button(root, text='Insert to Database', command=insertDb, pady=5)
createDatabase = Button(root, text='Click to Create DB', command=createDb, state=DISABLED)
showDatabase = Button(root, text='Show database', command=showDb, pady=5)
deleteButton = Button(root, text="Delete a Book", command=deleteBook)

# GRID THE LABEL
nome_livroLabel.grid(row=0, column=0, padx=10, pady=10)
autor_livroLabel.grid(row=1, column=0, padx=10, pady=10)
fileiraLabel.grid(row=2, column=0, padx=10, pady=10)
oidLabel.grid(row=5, column=0, padx=10, pady=10)

# GRID THE ENTRY
nomeEntry.grid(row=0, column=1, padx=10, pady=10)
autorEntry.grid(row=1, column=1, padx=10, pady=10)
fileiraEntry.grid(row=2, column=1, padx=10, pady=10)
oidSelect.grid(row=5, column=1)

# GRID THE BUTTONS
insertIntoDb.grid(row=3, column=0, columnspan=2, ipadx=125)
showDatabase.grid(row=4, column=0, columnspan=2, ipadx=132, pady=10)
deleteButton.grid(row=6, column=0, columnspan=2, ipadx=134, pady=10)
createDatabase.grid(row=7, column=1, sticky='se', pady=50, padx=10)

root.mainloop()