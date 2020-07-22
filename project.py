from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from tkcalendar import DateEntry


def addbtn():

	if contact.get() =='' or name.get()=='' or restime.get()=='' or persons.get() =='' or table.get()=='' or valchk.get()=='':
		messagebox.showerror("INVALID ENTRY","ENTER ALL FIELD")

	else:
		listbox.insert(END,(cal.get(),"|",name.get(),"(",contact.get(),")->",valchk.get(),"-",restime.get(),"-(TABLE)",table.get(),"-(PERSONS)",persons.get()))
		

def delbtn():
	listbox.delete(ANCHOR)
	

def clrbtn():
	name_entry.delete(0,END)
	contact_entry.delete(0,END)
	persons_entry.delete(0,END)
	restime_entry.delete(0,END)
	tabno_entry.delete(0,END)
	chk1.deselect()
	chk2.deselect()
	chk3.deselect()
    


root = Tk()
root.geometry('590x400')
root.title('RESTRAUTANT RESERVATIONS')
root.resizable(False,False)
root.configure(bg='#373F51')

# customer name
name_label = Label(root, text = 'NAME',bg='#373F51',font=("Helvetica",10,'bold'),fg="#FFFFFF")
name_label.grid(row = 0, column = 0, pady = 10,padx = 15)
name = StringVar()
name_entry = Entry(root, width=30, textvariable= name,bd=2)
name_entry.grid(row=0, column =1)

# customer contact
contact_label = Label(root, text = 'CONTACT NO.',bg='#373F51',font=("Helvetica",10,'bold'),fg="#FFFFFF")
contact_label.grid(row = 1, column = 0, padx= 15, pady = 10)
contact = StringVar()
contact_entry = Entry(root,width=30, textvariable= 	contact,bd=2)
contact_entry.grid(row=1, column =1)


# reservation time
restime_label = Label(root, text = 'RESERVATION TIME',bg='#373F51',font=("Helvetica",10,'bold'),fg="#FFFFFF")
restime_label.grid(row = 2, column = 0, padx = 0, pady = 20)
restime = StringVar()
restime_entry = Entry(root,width=30, textvariable = restime,bd=2)
restime_entry.grid(row=2, column =1)


# number of persons
persons_label = Label(root, text = 'PERSONS',bg='#373F51',font=("Helvetica",10,'bold'),fg="#FFFFFF")
persons_label.grid(row = 0, column = 2, padx = 30)
persons = StringVar()
persons_entry = Entry(root,width=5, textvariable = persons,bd=2)
persons_entry.grid(row=0, column =3)

# table number
tabno_label = Label(root, text = 'TABLE NO.',bg='#373F51',font=("Helvetica",10,'bold'),fg="#FFFFFF")
tabno_label.grid(row = 1, column = 2, padx = 30)
table = StringVar()
tabno_entry = Entry(root,width=5, textvariable = table,bd=2)
tabno_entry.grid(row=1, column =3)

#reservation date
resdate = Label(root, text = 'RESERVATION DATE',bg='#373F51',font=("Helvetica",10,'bold'),fg="#FFFFFF")
resdate.grid(row = 2, column = 2, padx = 15)

#buttons
# add button
add_btn = Button(root, text='ADD ENTRY', command = addbtn,relief=GROOVE, bg='#9AFF1F',fg="#000000")
add_btn.grid(row = 4, column =0, pady = 10)
#delete button
del_btn = Button(root, text='DELETE ENTRY', command = delbtn,relief=GROOVE, bg='#9AFF1F',fg="#000000")
del_btn.grid(row = 4, column =1, pady = 10)
#clear input button
clr_btn = Button(root, text='CLEAR INPUT', command = clrbtn,relief=GROOVE, bg='#9AFF1F',fg="#000000")
clr_btn.grid(row = 4, column =2, pady = 10)
#quit button
quit_btn = Button(root, text='QUIT', command = quit,relief=GROOVE, bg='#9AFF1F',fg="#000000")
quit_btn.grid(row=4, column= 3 , pady = 10)

#dropdown calender
cal = DateEntry(root, width=12, year=2020, month=7, day=22,bg='#9AFF1F', fg="#000000", borderwidth=2)
cal.grid(row = 2,column = 3)

#listbox and scrollbar
listbox = Listbox(root, width = 80, height = 10)
listbox.grid(row = 5, columnspan = 4) 
scroll_y = Scrollbar(root,orient = VERTICAL,bg='black')
scroll_y.grid(row=5, column=3,sticky='ns')
listbox.configure(yscrollcommand= scroll_y.set)
scroll_y.configure(command= listbox.yview)


#checkboxes
valchk = StringVar()
chk1 = Checkbutton(root, text = "BREAKFAST", variable = valchk , onvalue= "BREAKFAST", offvalue = "")
chk1.grid(row = 3, column = 0)
chk2 = Checkbutton(root, text = "LUNCH", variable = valchk , onvalue= "LUNCH", offvalue = "")
chk2.grid(row = 3, column = 1)
chk3 = Checkbutton(root, text = "DINNER", variable = valchk , onvalue= "DINNER", offvalue = "")
chk3.grid(row = 3, column = 2)


root.mainloop()