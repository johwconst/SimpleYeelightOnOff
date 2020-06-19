#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import database
import tkinter as tk
import tkinter.ttk as tkk
from tkinter import messagebox
from yeelight import Bulb

class mainWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        master.title('Simple Yeelight On/Off - CRUD')
        master.geometry("+{}+{}".format(200, 200))

        # instance database
        self.db = database.createDB()
        self.pack()

        # Create Window
        self.createWid()

    def createWid(self):
        # Create frames
        frame1 = tk.Frame(self)
        frame1.pack(side=tk.TOP, fill=tk.BOTH, padx=160, pady=10, anchor='center')

        frame2 = tk.Frame(self)
        frame2.pack(fill=tk.BOTH, expand=True, padx=15)

        frame3 = tk.Frame(self)
        frame3.pack(side=tk.BOTTOM, padx=5)

        # Labels
        name_label = tk.Label(frame1, text='Name *')
        name_label.grid(row=0, column=0)

        ip_label = tk.Label(frame1, text='IP *')
        ip_label.grid(row=0, column=1)

        location_label = tk.Label(frame1, text='Location')
        location_label.grid(row=0, column=2)

        # Entry Text
        self.req_name = tk.Entry(frame1)
        self.req_name.grid(row=1, column=0)

        self.req_ip = tk.Entry(frame1)
        self.req_ip.grid(row=1, column=1, padx=10)

        self.req_location = tk.Entry(frame1)
        self.req_location.grid(row=1, column=2)

        # Add Button
        button_add = tk.Button(frame1, text='Add Yeelight', bg='#FF6700', fg='black')
        button_add['font'] = ("Arial", "12", "bold")
        button_add['command'] = self.addLamp
        button_add.grid(row=0, column=4, rowspan=2, padx=10)

        # Treeview.
        self.treeview = tkk.Treeview(frame2, columns=('Nome', 'IP', 'Localização'))
        self.treeview.heading('#0', text='ID')
        self.treeview.heading('#1', text='Name')
        self.treeview.heading('#2', text='IP')
        self.treeview.heading('#3', text='Location')

        for row in self.db.getLamp():
            self.treeview.insert('', 'end', text=row[0], values=(row[1], row[2], row[3]))

        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Delete Button
        button_delete = tk.Button(frame3, text='Delete', bg='#E71818', fg='white')
        button_delete['font'] = ("Arial", "12", "bold")
        button_delete['command'] = self.deleteLamp
        button_delete.pack(side='left', padx=10, pady=10)

        # Turn On Button
        button_on = tk.Button(frame3, text="Turn On", bg="black", fg='white')
        button_on['font'] = ("Arial", "12", "bold")
        button_on['command'] = self.turnOn
        button_on.pack(side='left', padx=10, pady=10)

        # Turn Off Button
        button_off = tk.Button(frame3, text="Turn Off", bg="black", fg='white')
        button_off['font'] = ("Arial", "12", "bold")
        button_off['command'] = self.turnOff
        button_off.pack(side='left', padx=10, pady=10)

    def turnOn(self):
        if not self.treeview.focus():
            messagebox.showwarning('Ops..', 'No item selected')
        else:
            select_lamp = self.treeview.focus()
            res = self.treeview.item(select_lamp)
            ip = res['values'][1]
            print(ip)
            bulb = Bulb(ip)
            bulb.turn_on()

    def turnOff(self):
        if not self.treeview.focus():
            messagebox.showwarning('Ops..', 'No item selected')
        else:
            select_lamp = self.treeview.focus()
            res = self.treeview.item(select_lamp)
            ip = res['values'][1]
            bulb = Bulb(ip)
            bulb.turn_off()

    def addLamp(self):
        name = self.req_name.get()
        ip = self.req_ip.get()
        location = self.req_location.get()

        self.db.addLamp(name=name, ip=ip, location=location)
        id = self.db.getLastLamp()[0]
        self.treeview.insert('', 'end', text=id, values=(name, ip, location))

    def deleteLamp(self):
        if not self.treeview.focus():
            messagebox.showwarning('Ops..', 'No item selected')
        else:
            selected = self.treeview.focus()
            id = self.treeview.item(selected)
            self.db.deleteLamp(id['text'])
            self.treeview.delete(selected)

root = tk.Tk()
root.iconbitmap('icon.ico')
app = mainWindow(master=root)
app.mainloop()