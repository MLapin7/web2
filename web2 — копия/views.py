import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()


    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd = 2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        self.add_img = tk.PhotoImage(file='./img/add.png')
        btn_open_dialog = tk.Button(toolbar, bg='#d7d8e0', bd=0, image=self.add_img, command = self.open_dialog)
        btn_open_dialog.pack(side = tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'name', 'tel', 'e-mail'), height=45, show='headings')
        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("name", width=300, anchor=tk.CENTER)
        self.tree.column("tel", width=150, anchor=tk.CENTER)
        self.tree.column("e-mail", width=150, anchor=tk.CENTER)

        self.tree.heading("ID", text='ID')
        self.tree.heading("name", text='ФИО')
        self.tree.heading("tel", text='Телефон')
        self.tree.heading("e-mail", text='E-mail')

        self.tree.pack(side=tk.LEFT)


    def open_dialog(self):
        Child


class Child(tk.Toplevel):
    def __init__(self):
        super.__init__(root)
        self.init_child()



    def init_child(self):
        self.title('Добавить')
        self.geometry('400x200')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set

        label_name = tk.Label(self, text='ФИО:')
        label_name.place(x=50, y=50)
        label_select = tk.Label(self, text='Телефон')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='E-mail')
        label_sum.place(x=50, y=110)

        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=200, y=50)
        self.entry_tel = ttk.Entry(self)
        self.entry_tel.place(x=200, y=110)
        self.entry_email = ttk.Entry(self)
        self.entry_email.place(x=200, y=80)

        self.btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        self.btn_cancel(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=300, y=170)





if __name__ == 'main':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('Телефонная книга')
    root.geometry('665x450')
    root.resizable(False, False)
    root.mainloop()