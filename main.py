# Import Modules
from tkinter import *
from tkinter import font
from tkinter import filedialog
import webbrowser
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import font, ttk
from tkinter import colorchooser

root = Tk()
root.title("PolarNotes")
root.iconbitmap('icon.ico')
root.geometry("1200x700")
root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "dark")
root.resizable(False, False)
# Setting global variable for open file name
global open_status_name
global selected
selected = False
open_status_name = False

# Open Github Repo
new = 1
url = "https://github.com/NotsoFrostyy/PolarNotes"


def openweb():
    webbrowser.open(url, new=new)

# About tile


def about():
    messagebox.showinfo(
        'Frost Software', 'PolarNotes is an experimental notepad containing advanced features, find out more at the github repo at @Notsofrostyy')

# New file creation


def filenew():
    # Delete previous text
    text.delete("1.0", END)
    root.title('New File - PolarNotes')
    global open_status_name
    open_status_name = False

# Open file


def fileopen():
    # Delete previous text
    text.delete("1.0", END)
    # Grab file name
    text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    if text_file:
        # make filename global so we can access it
        global open_status_name
        open_status_name = text_file

    # update status bars
    name = text_file
    root.title(f'Opened: {name}        ')
    name.replace("C:/", "")
    root.title(f'{name} - PolarNotes')

    # open file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # add file to textbox
    text.insert(END, stuff)
    # close the opened file
    text_file.close()


def filesaveas():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/desktop/", title="Save File", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # update status bars
        name = text_file
        root.title(f'Saved As: {name}        ')
        name = name.replace("C:/desktop/", "")
        root.title(f'{name} - PolarNotes')

        # save file
        text_file = open(text_file, 'w')
        text_file.write(text.get(1.0, END))
        text_file.close()

# Save file


def filesave(e):
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(text.get(1.0, END))
        text_file.close()
        root.title(f'Saved: {open_status_name}        ')
    else:
        filesaveas()

# Cut Text


def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if text.selection_get():
            # Grab selected text from textbox
            selected = text.selection_get()
            # Delete selected text from textbox
            text.delete("sel.first", "sel.last")
            # clear clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)

# Copy Text


def copy_text(e):
    global selected
    # check to see if keyboard shortcuts were used
    if e:
        selected = root.clipboard_get()

    else:
        if text.selection_get():
            selected = text.selection_get()
            # clear clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)

# Paste Text


def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get
    else:
        if selected:
            position = text.index(INSERT)
            text.insert(position, selected)

# Search With Youtube


def ytsearch(e):
    global selected
    if text.selection_get():
        # Grab selected text from textbox
        selected = text.selection_get()
        s = str(selected).replace("yt", "")
        link = "https://www.youtube.com/results?search_query=" + s
        webbrowser.open_new_tab(link)


def gitsearch(e):
    global selected
    if text.selection_get():
        # Grab selected text from textbox
        selected = text.selection_get()
        s = str(selected.replace("git", ""))
        link = "https://github.com/search?q=" + s
        webbrowser.open_new_tab(link)


def dckdckgosearch(e):
    global selected
    if text.selection_get():
        # Grab selected text from textbox
        selected = text.selection_get()
        s = str(selected.replace("duckduckgo", ""))
        link = "https://duckduckgo.com/?q=" + s
        webbrowser.open_new_tab(link)


def shortcuts():
    messagebox.showinfo(
        "Shorcuts", "CTRL+G - Search With Github \nCTRL+E - Search With Youtube \nCTRL+H - Search with DuckDuckGo")


def BoldIt():
    # Create font
    bold_font = font.Font(text, text.cget("font"))
    bold_font.configure(weight="bold")

    # Configure Tag
    text.tag_configure("bold", font=bold_font)
    # create current tag var
    current_tags = text.tag_names("sel.first")
    # if statmenmet to see if tag has been set/used
    if "bold" in current_tags:
        text.tag_remove("bold", "sel.first", "sel.last")
    else:
        text.tag_add("bold", "sel.first", "sel.last")


def ItalicIt():
    italic_font = font.Font(text, text.cget("font"))
    italic_font.configure(slant="italic")

    # Configure Tag
    text.tag_configure("italic", font=italic_font)
    # create current tag var
    current_tags = text.tag_names("sel.first")
    # if statmenmet to see if tag has been set/used
    if "italic" in current_tags:
        text.tag_remove("italic", "sel.first", "sel.last")
    else:
        text.tag_add("italic", "sel.first", "sel.last")


def text_color():
    colorset = colorchooser.askcolor()[1]
    if colorset:
        color_font = font.Font(text, text.cget("font"))

        # Configure Tag
        text.tag_configure("colored", font=color_font, foreground=colorset)
        # create current tag var
        tags_set = text.tag_names("sel.first")
        # if statmenmet to see if tag has been set/used
        if "colored" in tags_set:
            text.tag_remove("colored", "sel.first", "sel.last")
        else:
            text.tag_add("colored", "sel.first", "sel.last")


def all_text_colour():
    colorset = colorchooser.askcolor()[1]
    if colorset:
        text.config(fg=colorset)


def select_all(e):
    # Add sel Tag to select all text
    text.tag_add('sel', '1.0', 'end')


def clear_all():
    text.delete(1.0, END)


def update(event):
    status.config(text="Word Count: " +
                  str(len(text.get("1.0", 'end-1c'))))


# create toolbar frame
toolbar = Frame(root)
toolbar.pack(fill=X)


# create main frame
frame = Frame(root)
frame.pack()

# scroll bar for text box
text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)

hor_text_scroll = Scrollbar(frame, orient='horizontal')
hor_text_scroll.pack(side=BOTTOM, fill=X)

# create text box
text = Text(frame, width=100, height=25, font=("Arial", 16), fg="White", bg="#1e2124",
            selectforeground="white", undo=True, yscrollcommand=text_scroll.set, xscrollcommand=hor_text_scroll.set, wrap="none")
text.pack()

# scroll conmfig
text_scroll.config(command=text.yview)
hor_text_scroll.config(command=text.xview)


# menu bar
menu = Menu(root)
root.config(menu=menu, bg="#555555")

# add file menu
file_menu = Menu(menu, tearoff=False,)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=filenew)
file_menu.add_command(label="Open", command=fileopen)
file_menu.add_command(label="Save", command=lambda: filesave(False))
file_menu.add_command(label="Save As", command=filesaveas)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# add edit menu
edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(
    False), accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=lambda: copy_text(
    False), accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=lambda: paste_text(
    False), accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(
    label="Undo", command=text.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(
    label="Redo", command=text.edit_redo, accelerator="Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Search with Youtube",
                      command=lambda: ytsearch(''), accelerator="Ctrl+E")
edit_menu.add_command(label="Search with Github",
                      command=lambda: gitsearch(''), accelerator="Ctrl+G")
edit_menu.add_command(label="Search with DuckDuckGo",
                      command=lambda: dckdckgosearch(''), accelerator="Ctrl+H")
edit_menu.add_separator()
edit_menu.add_command(label="Select All",
                      command=lambda: select_all(False), accelerator="Ctrl+A")
edit_menu.add_command(
    label="Clear All", command=clear_all, accelerator="Ctrl+")

# Tools Menu
tools_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(
    label="Change color of selected Text ", command=text_color)
tools_menu.add_command(label="Change color of All Text",
                       command=all_text_colour)
tools_menu.add_separator()
tools_menu.add_command(label="Bold Selected Text", command=BoldIt)
tools_menu.add_command(label="Italic Selected Text", command=ItalicIt)

# Help menu
help_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Github Repo", command=openweb)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="Shortcut", command=shortcuts)

# edit binding
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-e>', ytsearch)
root.bind('<Control-Key-g>', gitsearch)
root.bind('<Control-Key-h>', dckdckgosearch)
root.bind('<Control-Key-a>', select_all)
root.bind('<Control-Key-a>', select_all)
root.bind('<Control-Key-s>', filesave)
text.bind('<KeyPress>', update)
text.bind('<KeyRelease>', update)

# create buttons for toolbar

undo_icon = PhotoImage(file='icon_undo.png')
redo_icon = PhotoImage(file='icon_redo.png')
UndoBtn = Button(toolbar, image=undo_icon, command=text.edit_undo)
UndoBtn.grid(row=0, column=0, sticky=W, padx=5)

RedoBtn = Button(toolbar, image=redo_icon, command=text.edit_redo)
RedoBtn.grid(row=0, column=1, sticky=W, padx=5)


def click_theme():
    global root
    # WHEN CLICK IF THE THEME IS DARK IT SET TO LIGHT
    is_dark = root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark"
    if is_dark:
        root.tk.call("set_theme", "light")
        text.config(bg='white', foreground='#1e2124')
        theme_button.config(text="Dark Mode")
        status.config(background='white', foreground='#1e2124')
        file_menu.config(bg="white", fg='#1e2124')
        edit_menu.config(bg="white", fg='#1e2124')
        tools_menu.config(bg="white", fg='#1e2124')
        help_menu.config(bg="white", fg='#1e2124')

    else:
        root.tk.call("set_theme", "dark")
        text.config(bg='#1e2124', fg='white')
        theme_button.config(text="Light Mode")
        status.config(background='#1e2124', foreground='white')
        file_menu.config(bg="#1e2124", fg='white')
        edit_menu.config(bg="#1e2124", fg='white')
        tools_menu.config(bg="#1e2124", fg='white')
        help_menu.config(bg="#1e2124", fg='white')


theme_button = ttk.Button(toolbar, text="Light Mode", command=click_theme)
theme_button.grid(row=0, column=2, sticky=E, padx=5)

status = Label(root, text='Word Count: 0 ', anchor=W,
               background="#1e2124", foreground="white",)
status.pack(fill=X, side=BOTTOM, ipady=15)

root.mainloop()
