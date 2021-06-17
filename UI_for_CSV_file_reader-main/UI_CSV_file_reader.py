from tkinter import*
from tkinter import ttk
import csv
#Defining the Title and Geometry of the UI
root=Tk()
root.title('Personal Data information Centre')
frame=LabelFrame(root,padx=30,pady=30).grid()
Label_1=Label(frame,text="Open your files",font=("Times new roman",24)
,fg="white",bg="brown")
Label_1.grid(row=1,column=1,pady=20)
root.geometry("650x250")
#list of files
files=["file1","file2","file3","file4"]
text_1=Label(root,text="File Name :").grid()
text_2=Label(root,text="Name of person :").grid(padx=10)
def file_function(event):

	if clicked2.get()=="file1":
		clicked.config(value=name_1)
	elif clicked2.get()=="file2":
		clicked.config(value=name_2)
	elif clicked2.get()=="file3":
		clicked.config(value=name_3)
	elif clicked2.get()=="file4":
		clicked.config(value=name_4)
	
def selected(event):

	if clicked2.get()=="file1":
		state=state_name_1
		age=age_1
		name=name_1
	elif clicked2.get()=="file2":
		state=state_name_2
		age=age_2
		name=name_2
	elif clicked2.get()=="file3":
		state=state_name_3
		age=age_3
		name=name_3
	elif clicked2.get()=="file4":
		state=state_name_4
		age=age_4
		name=name_4

	for i in name:
		g=name.index(i)
		if clicked.get()==i:
			my_label.config(text=" {} is from {} and is {} years old"
			.format(i,state[g],age[g])
			,font=("Times", "12", "bold italic"))
		
global my_label	
my_label=Label(root,text="")
my_label.grid(row=22,column=1,pady=40)

#Defining the Comboboxes

clicked2=ttk.Combobox(root,value=files,state="readonly",width=20,height=50)
clicked2.bind("<<ComboboxSelected>>",file_function)
clicked2.grid(row=2,column=1,pady=10)

clicked=ttk.Combobox(root,value=[" "],state="readonly",width=20,height=50)
clicked.bind("<<ComboboxSelected>>",selected)
clicked.grid(row=3,column=1,pady=10)

#Reading the different CSV files and systematically listing them for extraction

#FILE-1

file1=open("file1.csv",'r')

rows_1=[]
name_1=[]
state_name_1=[]
age_1=[]

csvreader = csv.reader(file1)

for row in csvreader:
	rows_1.append(row)

for i in rows_1:
	name_1.append(i[0])
	state_name_1.append(i[1])
	age_1.append(i[2])

#FILE-2

file2=open("file2.csv",'r')

rows_2=[]
name_2=[]
state_name_2=[]
age_2=[]

csvreader_2 = csv.reader(file2)

for row_2 in csvreader_2:
	rows_2.append(row_2)

for k in rows_2:
	name_2.append(k[0])
	state_name_2.append(k[1])
	age_2.append(k[2])

#FILE-3

file3=open("file3.csv",'r')

rows_3=[]
name_3=[]
state_name_3=[]
age_3=[]

csvreader_3 = csv.reader(file3)

for row_3 in csvreader_3:
	rows_3.append(row_3)

for p in rows_3:
	name_3.append(p[0])
	state_name_3.append(p[1])
	age_3.append(p[2])

#FILE-4

file4=open("file4.csv",'r')

rows_4=[]
name_4=[]
state_name_4=[]
age_4=[]

csvreader_4 = csv.reader(file4)

for row_4 in csvreader_4:
	rows_4.append(row_4)

for q in rows_4:
	name_4.append(q[0])
	state_name_4.append(q[1])
	age_4.append(q[2])


root.mainloop()