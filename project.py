from tkinter import *
from tkinter import messagebox


def addbtn():

	if contact.get() =='' or name.get()=='' or restime.get()=='' or persons.get() =='' or table.get()=='':
		messagebox.showerror("field required","enter all fields")
	else:
		listbox.insert(END,([name.get()],contact.get(),restime.get(),persons.get(),table.get()))
		

def delbtn():
	listbox.delete(ANCHOR)
	

def clrbtn():
	name_entry.delete(0,END)
	contact_entry.delete(0,END)
	persons_entry.delete(0,END)
	restime_entry.delete(0,END)
	tabno_entry.delete(0,END)


root = Tk()
root.geometry('600x400')
root.title('DINNER RESERVATIONS')
root.resizable(False,False)

# customer name
name_label = Label(root, text = 'NAME')
name_label.grid(row = 0, column = 0, pady = 10,padx = 15)
name = StringVar()
name_entry = Entry(root, width=30, textvariable= name)
name_entry.grid(row=0, column =1)

# customer contact
contact_label = Label(root, text = 'CONTACT NO.')
contact_label.grid(row = 1, column = 0, padx= 15, pady = 10)
contact = StringVar()
contact_entry = Entry(root,width=30, textvariable= 	contact)
contact_entry.grid(row=1, column =1)


# reservation time
restime_label = Label(root, text = 'RESERVATION TIME')
restime_label.grid(row = 2, column = 0, padx = 0, pady = 20)
restime = StringVar()
restime_entry = Entry(root,width=30, textvariable = restime)
restime_entry.grid(row=2, column =1)


# number of persons
persons_label = Label(root, text = 'PERSONS')
persons_label.grid(row = 0, column = 2, padx = 30)
persons = StringVar()
persons_entry = Entry(root,width=5, textvariable = persons)
persons_entry.grid(row=0, column =3)

# table number
tabno_label = Label(root, text = 'TABLE NO.')
tabno_label.grid(row = 1, column = 2, padx = 30)
table = StringVar()
tabno_entry = Entry(root,width=5, textvariable = table)
tabno_entry.grid(row=1, column =3)

#buttons
# add button
add_btn = Button(root, text='Add entry', command = addbtn)
add_btn.grid(row = 3, column =0, pady = 10)
#delete button
del_btn = Button(root, text='Delete entry', command = delbtn)
del_btn.grid(row = 3, column =1, pady = 10)
#clear input button
clr_btn = Button(root, text='Clear input', command = clrbtn)
clr_btn.grid(row = 3, column =3, pady = 10)

#listbox
listbox = Listbox(root, width = 70, height = 10)
listbox.grid(row = 4, columnspan = 5) 
scroll = Scrollbar(root,orient = VERTICAL)
scroll.grid(row=4, column=3,sticky='ns')
listbox.configure(yscrollcommand= scroll.set)
scroll.configure(command= listbox.yview)




root.mainloop()