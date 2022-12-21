# Import Modules
from tkinter import *
from tkinter import font
from tkinter import filedialog
import webbrowser
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import font, ttk
from tkinter import colorchooser

# Application Base
root = Tk()
root.title("PolarNotes")
root.iconbitmap('icon.ico')
root.geometry("1400x800+200+200")
root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "dark")
root.state('normal')
root.resizable(True, True)


# Setting up global variables
global open_status_name
global selected
global font1

font1 = ['Arial', 16]
selected = False
open_status_name = False

# right click menu


def rclick_menu(event):
    try:
        rightClick_menu.tk_popup(event.x_root, event.y_root)

    finally:
        rightClick_menu.grab_release()

# Open Github Repo


def openweb():
    webbrowser.open_new_tab("https://github.com/NotsoFrostyy/PolarNotes")

# About Tile


def about():
    messagebox.showinfo(
        'Frost Software', 'PolarNotes is an experimental notepad containing advanced features, find out more at the github repo at @Notsofrostyy')


def current_version():
    messagebox.showinfo('Current Version', 'V1.0.1')

# bug report function


def bug_report():
    webbrowser.open_new_tab(
        "https://github.com/NotsoFrostyy/PolarNotes/issues/new")

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
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("JavaScript files", ".js"), ("All Files", "*.*")))

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

# Save file as


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
        # update status bars
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

# Search with Github


def gitsearch(e):
    global selected
    if text.selection_get():
        # Grab selected text from textbox
        selected = text.selection_get()
        s = str(selected.replace("git", ""))
        link = "https://github.com/search?q=" + s
        webbrowser.open_new_tab(link)

# Search with DuckDuckGo


def dckdckgosearch(e):
    global selected
    if text.selection_get():
        # Grab selected text from textbox
        selected = text.selection_get()
        s = str(selected.replace("duckduckgo", ""))
        link = "https://duckduckgo.com/?q=" + s
        webbrowser.open_new_tab(link)

# Shortcuts tile


def shortcuts():
    messagebox.showinfo(
        "Shorcuts", "CTRL+G - Search With Github \nCTRL+E - Search With Youtube \nCTRL+H - Search with DuckDuckGo")

# Bold Slected Text


def BoldText():
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

# italic selected text


def ItalicText():
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

# Change Text Color


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

# Change Color of all text


def all_text_color():
    colorset = colorchooser.askcolor()[1]
    if colorset:
        text.config(fg=colorset)

# Select all text


def select_all(e):
    # Add sel Tag to select all text
    text.tag_add('sel', '1.0', 'end')

# Clear all text


def clear_all():
    text.delete(1.0, END)

# Word count


def update(event):
    BottomBar.config(text="Word Count: " +
                     str(len(text.get("1.0", 'end-1c'))))

# Zoom


def Zoomed(zoom_input):
    global font1

    if(zoom_input == 'plus'):
        font1[1] = font1[1]+2
    else:
        font1[1] = font1[1]-2

    text.config(font=font1)

# Reset Zoom


def reset_font_size():
    global font1
    font1[1] = 16
    text.config(font=('Arial', 16))


def reset_window():
    root.geometry("1400x800+200+200")


# create toolbar frame
toolbar = Frame(root, height=50)
toolbar.pack(fill=X)

# scroll bar for text box
text_scroll = Scrollbar(root)
text_scroll.pack(side=RIGHT, fill=Y)

# create text box
text = Text(root, borderwidth=0, height=48, font=font1, fg="White", bg="#1e2124",
            selectforeground="white", undo=True, yscrollcommand=text_scroll.set, wrap="none")
text.focus_set()


# scroll config
text_scroll.config(command=text.yview)


# menu bar
menu = Menu(root)
root.config(menu=menu, bg="#1e2124")

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
                       command=all_text_color)
tools_menu.add_separator()
tools_menu.add_command(label="Bold Selected Text", command=BoldText)
tools_menu.add_command(label="Italic Selected Text", command=ItalicText)
tools_menu.add_separator()
tools_menu.add_command(label="Search with Youtube",
                       command=lambda: ytsearch(''), accelerator="Ctrl+E")
tools_menu.add_command(label="Search with Github",
                       command=lambda: gitsearch(''), accelerator="Ctrl+G")
tools_menu.add_command(label="Search with DuckDuckGo",
                       command=lambda: dckdckgosearch(''), accelerator="Ctrl+H")


# Window menu
view_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom In", command=lambda: Zoomed('plus'))
view_menu.add_command(label="Zoom Out", command=lambda: Zoomed('minus'))
view_menu.add_command(label="Reset Zoom", command=reset_font_size)
view_menu.add_separator()
view_menu.add_command(label="Reset Window", command=reset_window)

# Help menu
help_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Github Repo", command=openweb)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="Shortcut", command=shortcuts)
help_menu.add_command(label="Bug Report", command=bug_report)
help_menu.add_separator()
help_menu.add_command(label="Current Version", command=current_version)

# edit binding
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-e>', ytsearch)
root.bind('<Control-Key-g>', gitsearch)
root.bind('<Control-Key-h>', dckdckgosearch)
root.bind('<Control-Key-a>', select_all)
root.bind('<Control-Key-s>', filesave)
text.bind('<KeyPress>', update)
text.bind('<KeyRelease>', update)
text.bind("<Button - 3>", rclick_menu)

# Undo And redo
undo_icon = PhotoImage(file='icon_undo.png')
redo_icon = PhotoImage(file='icon_redo.png')
UndoBtn = Button(toolbar, image=undo_icon, command=text.edit_undo)
UndoBtn.grid(row=0, column=0, sticky=W, padx=5)

RedoBtn = Button(toolbar, image=redo_icon, command=text.edit_redo)
RedoBtn.grid(row=0, column=1, sticky=W, padx=5)

# Changing Theme


def click_theme():
    global root
    # WHEN CLICK IF THE THEME IS DARK IT SET TO LIGHT
    is_dark = root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark"
    if is_dark:
        root.tk.call("set_theme", "light")
        text.config(bg='white', foreground='#1e2124')
        theme_button.config(text="Dark Mode")
        BottomBar.config(background='white', foreground='#1e2124')
        file_menu.config(bg="white", fg='#1e2124')
        edit_menu.config(bg="white", fg='#1e2124')
        tools_menu.config(bg="white", fg='#1e2124')
        help_menu.config(bg="white", fg='#1e2124')
        view_menu.config(bg="white", fg='#1e2124')
        root.config(bg="white")
        rightClick_menu.config(bg="white", fg='#1e2124')

    else:
        root.tk.call("set_theme", "dark")
        text.config(bg='#1e2124', fg='white')
        theme_button.config(text="Light Mode")
        BottomBar.config(background='#1e2124', foreground='white')
        file_menu.config(bg="#1e2124", fg='white')
        edit_menu.config(bg="#1e2124", fg='white')
        tools_menu.config(bg="#1e2124", fg='white')
        help_menu.config(bg="#1e2124", fg='white')
        view_menu.config(bg="#1e2124", fg='white')
        root.config(bg="#1e2124")
        rightClick_menu.config(bg="#1e2124", fg='white')


theme_button = ttk.Button(toolbar, text="Light Mode", command=click_theme)
theme_button.grid(row=0, column=2, sticky=E, padx=5)

# Setting Right click menu
rightClick_menu = Menu(text, tearoff=0, bg="#1e2124")

rightClick_menu.add_command(label="Cut", command=lambda: cut_text(
    False))
rightClick_menu.add_command(label="Copy", command=lambda: copy_text(
    False))
rightClick_menu.add_command(label="Paste", command=lambda: paste_text(
    False))
rightClick_menu.add_separator()
rightClick_menu.add_command(
    label="Undo", command=text.edit_undo, accelerator="Ctrl+Z")
rightClick_menu.add_command(
    label="Redo", command=text.edit_redo, accelerator="Ctrl+Y")
rightClick_menu.add_separator()
rightClick_menu.add_command(label="Search with Youtube",
                            command=lambda: ytsearch(''), accelerator="Ctrl+E")
rightClick_menu.add_command(label="Search with Github",
                            command=lambda: gitsearch(''), accelerator="Ctrl+G")
rightClick_menu.add_command(label="Search with DuckDuckGo",
                            command=lambda: dckdckgosearch(''), accelerator="Ctrl+H")
rightClick_menu.add_separator()
rightClick_menu.add_command(label="Select All",
                            command=lambda: select_all(False), accelerator="Ctrl+A")
rightClick_menu.add_command(
    label="Clear All", command=clear_all, accelerator="Ctrl+")

# Status bar and Bottom Bar
BtmFrame = Frame(root, height=10)
BtmFrame.pack(side=BOTTOM, fill=X)

BottomBar = Label(BtmFrame, text='Word Count: 0 ',
                  background="#1e2124", foreground="white", font=(24))
BottomBar.pack(side=LEFT)


text.pack(fill=BOTH, side=TOP)
root.mainloop()
