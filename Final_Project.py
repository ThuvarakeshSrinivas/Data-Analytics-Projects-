from tkinter import *
import tkinter.messagebox
import sqlite3

# Create main window
root = Tk()
root.geometry('700x600')
root.title('Formula1 Paddock Entry')
root.config(background='light blue')

# Connect to SQLite database (or create it)
conn = sqlite3.connect('f1_paddock.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS paddock_entry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    constructor TEXT,
    engine TEXT,
    paddock_members TEXT,
    gender TEXT)
''')
conn.commit()

# Variables
fn = StringVar()
ln = StringVar()
constructor = StringVar()
var = StringVar()
radio_var = StringVar()

var_c1 = IntVar()
var_c2 = IntVar()
var_c3 = IntVar()

selected_id = None

# Reset form fields
def reset_form():
    fn.set("")
    ln.set("")
    constructor.set("")
    var.set("Select Engine")
    radio_var.set("")
    var_c1.set(0)
    var_c2.set(0)
    var_c3.set(0)

# Load all entries into the listbox
def load_entries():
    listbox.delete(0, END)
    cursor.execute("SELECT id, first_name, last_name FROM paddock_entry")
    for row in cursor.fetchall():
        listbox.insert(END, f"{row[0]} - {row[1]} {row[2]}")

# When listbox item is selected, populate form
def on_select(event):
    global selected_id
    if not listbox.curselection():
        return
    index = listbox.curselection()[0]
    entry_text = listbox.get(index)
    selected_id = int(entry_text.split(' - ')[0])

    # Get full details from DB
    cursor.execute("SELECT * FROM paddock_entry WHERE id=?", (selected_id,))
    row = cursor.fetchone()
    if row:
        fn.set(row[1])
        ln.set(row[2])
        constructor.set(row[3])
        var.set(row[4])
        radio_var.set(row[6])  # gender

        # Set checkboxes based on stored string
        var_c1.set(0)
        var_c2.set(0)
        var_c3.set(0)
        members = row[5].split(", ")
        if "Drivers" in members:
            var_c1.set(1)
        if "Team Members" in members:
            var_c2.set(1)
        if "Others" in members:
            var_c3.set(1)

# Delete selected entry
def delete_entry():
    global selected_id
    if selected_id is None:
        tkinter.messagebox.showwarning("Selection Error", "Please select an entry to delete.")
        return
    confirm = tkinter.messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this entry?")
    if confirm:
        cursor.execute("DELETE FROM paddock_entry WHERE id=?", (selected_id,))
        conn.commit()
        tkinter.messagebox.showinfo("Deleted", "Entry deleted successfully.")
        selected_id = None
        reset_form()
        load_entries()

# Add new entry
def printent():
    first = fn.get()
    second = ln.get()
    team = constructor.get()
    engine = var.get()
    gender = radio_var.get()

    paddock_members = []
    if var_c1.get():
        paddock_members.append("Drivers")
    if var_c2.get():
        paddock_members.append("Team Members")
    if var_c3.get():
        paddock_members.append("Others")
    paddock_str = ", ".join(paddock_members)

    if first == "" or second == "" or team == "" or engine == "Select Engine" or gender == "":
        tkinter.messagebox.showwarning("Input Error", "Please fill all required fields.")
        return

    # Insert into database
    cursor.execute('''
        INSERT INTO paddock_entry (first_name, last_name, constructor, engine, paddock_members, gender)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (first, second, team, engine, paddock_str, gender))
    conn.commit()

    tkinter.messagebox.showinfo('Success', 'User has successfully signed up!')
    reset_form()
    load_entries()

# Update selected entry
def update_entry():
    global selected_id
    if selected_id is None:
        tkinter.messagebox.showwarning("Selection Error", "Please select an entry to update.")
        return

    first = fn.get()
    second = ln.get()
    team = constructor.get()
    engine = var.get()
    gender = radio_var.get()

    paddock_members = []
    if var_c1.get():
        paddock_members.append("Drivers")
    if var_c2.get():
        paddock_members.append("Team Members")
    if var_c3.get():
        paddock_members.append("Others")
    paddock_str = ", ".join(paddock_members)

    if first == "" or second == "" or team == "" or engine == "Select Engine" or gender == "":
        tkinter.messagebox.showwarning("Input Error", "Please fill all required fields.")
        return

    cursor.execute('''
        UPDATE paddock_entry
        SET first_name=?, last_name=?, constructor=?, engine=?, paddock_members=?, gender=?
        WHERE id=?
    ''', (first, second, team, engine, paddock_str, gender, selected_id))
    conn.commit()

    tkinter.messagebox.showinfo('Updated', 'Entry updated successfully.')
    reset_form()
    load_entries()
    selected_id = None

# UI Design
Label(root, text='Formula 1 Paddock Form', relief=SOLID, width=25, font='arial 18 bold', fg='Dark Blue', bg='White').place(x=90, y=10)

Label(root, text="First Name:", width=20, font=("bold", 10), bg='White').place(x=80, y=70)
Entry(root, textvar=fn).place(x=260, y=70)

Label(root, text="Surname:", width=20, font=("bold", 10), bg='White').place(x=80, y=120)
Entry(root, textvar=ln).place(x=260, y=120)

Label(root, text="Constructor:", width=20, font=("bold", 10), bg='White').place(x=80, y=170)
Entry(root, textvar=constructor).place(x=260, y=170)

Label(root, text="Engine Manufacturer:", width=20, font=("bold", 10), bg='White').place(x=65, y=220)
engine_options = ["Mercedes", "Ferrari", "Renault", "Honda"]
OptionMenu(root, var, *engine_options).place(x=260, y=220)
var.set("Select Engine")

Label(root, text="Paddock Member:", width=20, font=("bold", 10), bg='White').place(x=95, y=270)
Checkbutton(root, text="Drivers", variable=var_c1, bg='light blue').place(x=235, y=270)
Checkbutton(root, text="Team Members", variable=var_c2, bg='light blue').place(x=330, y=270)
Checkbutton(root, text='Others', variable=var_c3, bg='light blue').place(x=440, y=270)

Label(root, text="Gender:", width=20, font=("bold", 10), bg='White').place(x=73, y=320)
Radiobutton(root, text="Male", variable=radio_var, value="Male", bg='light blue').place(x=230, y=320)
Radiobutton(root, text="Female", variable=radio_var, value="Female", bg='light blue').place(x=300, y=320)

Button(root, text='Submit', width=12, bg='White', fg='Black', command=printent).place(x=80, y=400)
Button(root, text='Update', width=12, bg='White', fg='Black', command=update_entry).place(x=200, y=400)
Button(root, text='Delete', width=12, bg='White', fg='Black', command=delete_entry).place(x=320, y=400)
Button(root, text='Quit', width=12, bg='White', fg='Black', command=root.quit).place(x=440, y=400)

# Listbox for entries
Label(root, text="Registered Entries:", font=("bold", 10), bg='light blue').place(x=80, y=450)
listbox = Listbox(root, width=60)
listbox.place(x=80, y=480)
listbox.bind('<<ListboxSelect>>', on_select)

# Initial load
load_entries()

# Close DB connection on exit
def on_closing():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
