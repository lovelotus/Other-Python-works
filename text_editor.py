from Tkinter import *
from tkSimpleDialog import askstring
from tkFileDialog   import asksaveasfilename,askopenfilename
from tkMessageBox import askokcancel 
    
class Lotus:
    def open_new_file(obj):
            obj.text.delete(0.0, END)

    def save_file_as(obj):
            filename = asksaveasfilename()
            alltext = obj.text.get(0.0, END)
            open(filename,'w').write(alltext)

    def open_existing_file(obj):
            filename = askopenfilename()
            f= open(filename,'r')
            alltext=f.read() 
            obj.text.delete(0.0, END)
            obj.text.insert(0.0, alltext)

    def exit_editor(obj):
        ans=askokcancel('Confirm exit...', 'Really wanna exit???...');
        if ans:
            global root
            obj.root.destroy()
    
    def __init__(obj):
            obj.root = Tk()
            obj.root.title("A Simple Text Editor : beginner")
            obj.root.minsize(width=600,height=500)
            menubar = Menu(obj.root)
            filemenu = Menu(menubar,tearoff=0)
            filemenu.add_command(label="New", command=obj.open_new_file, accelerator="Ctrl+N")
            filemenu.add_separator()
            filemenu.add_command(label="Open", command=obj.open_existing_file, accelerator="Ctrl+O")
            filemenu.add_separator()
            filemenu.add_command(label="Save", command=obj.save_file_as, accelerator="Ctrl+S")
            menubar.add_cascade(label="File", menu=filemenu)
            filemenu.add_separator()
            filemenu.add_command(label="Exit", command=obj.exit_editor, accelerator="Ctrl+Q")
            obj.root.config(menu=menubar)
            obj.text = Text(obj.root)
            obj.text.pack(expand=YES, fill=BOTH)

my_app = Lotus()
my_app.root.mainloop()
