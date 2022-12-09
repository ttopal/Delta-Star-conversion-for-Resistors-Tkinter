# Delta-Star Conversion
import tkinter as tk
import tkinter.ttk as ttk


class DeltaStarWidget(ttk.Panedwindow):
    def __init__(self, master=None, **kw):
        super(DeltaStarWidget, self).__init__(master, **kw)
        self.frame1 = ttk.Frame(self)
        self.frame1.configure(height=150, width=600)
        self.frame4 = ttk.Frame(self.frame1)
        self.frame4.configure(height=75, width=600)
        self.label1 = ttk.Label(self.frame4)
        self.label1.configure(
            anchor="center",
            background="#aaaaaa",
            font="{verdana} 13 {bold}",
            foreground="#0000a0",
            justify="center",
            relief="groove",
            text='DELTA-STAR CONVERSION')
        self.label1.pack(expand="true", fill="both", side="top")
        self.frame4.pack(expand="true", fill="both", side="top")
        self.frame5 = ttk.Frame(self.frame1)
        self.frame5.configure(height=75, width=600)
        self.label2 = ttk.Label(self.frame5)
        self.label2.configure(
            anchor="center",
            background="#800000",
            font="{verdana} 10 {bold}",
            foreground="#00ff00",
            text='DELTA-STAR')
        self.label2.pack(expand="true", fill="both", side="left")
        self.label3 = ttk.Label(self.frame5)
        self.label3.configure(
            anchor="center",
            background="#800000",
            font="{verdana} 10 {bold}",
            foreground="#008000",
            text='STAR-DELTA')
        self.label3.pack(expand="true", fill="both", side="right")
        self.frame5.pack(expand="true", fill="both", side="top")
        self.frame1.pack(side="top")
        self.add(self.frame1, weight="1")
        self.frame2 = ttk.Frame(self)
        self.frame2.configure(height=300, width=600)
        self.cn_entry = tk.Canvas(self.frame2)
        self.cn_entry.configure(height=300, width=600)
        self.cn_entry.pack(expand="true", fill="both", side="top")
        self.ent_Ra = ttk.Entry(self.frame2)
        self.ent_Ra.configure(width=10)
        _text_ = 'Ra'
        self.ent_Ra.delete("0", "end")
        self.ent_Ra.insert("0", _text_)
        self.ent_Ra.place(anchor="nw", relx=0.19, rely=0.29, x=0, y=0)
        self.ent_Ra.bind("<FocusIn>", lambda e:self.ent_Ra.delete("0","end"))
        self.ent_Rb = ttk.Entry(self.frame2)
        self.ent_Rb.configure(width=10)
        _text_ = 'Rb'
        self.ent_Rb.delete("0", "end")
        self.ent_Rb.insert("0", _text_)
        self.ent_Rb.place(anchor="nw", relx=0.29, rely=0.42, x=0, y=0)
        self.ent_Rb.bind("<FocusIn>", lambda e:self.ent_Rb.delete("0","end"))
        self.ent_Rc = ttk.Entry(self.frame2)
        self.ent_Rc.configure(width=10)
        _text_ = 'Rc'
        self.ent_Rc.delete("0", "end")
        self.ent_Rc.insert("0", _text_)
        self.ent_Rc.place(anchor="nw", relx=0.06, rely=0.42, x=0, y=0)
        self.ent_Rc.bind("<FocusIn>", lambda e:self.ent_Rc.delete("0","end"))
        self.ent_R1 = ttk.Entry(self.frame2)
        self.ent_R1.configure(width=10)
        _text_ = 'R1'
        self.ent_R1.delete("0", "end")
        self.ent_R1.insert("0", _text_)
        self.ent_R1.place(anchor="nw", relx=0.7, rely=0.19, x=0, y=0)
        self.ent_R1.bind("<FocusIn>", lambda e:self.ent_R1.delete("0","end"))
        self.ent_R2 = ttk.Entry(self.frame2)
        self.ent_R2.configure(exportselection="true", justify="left", width=10)
        _text_ = 'R2'
        self.ent_R2.delete("0", "end")
        self.ent_R2.insert("0", _text_)
        self.ent_R2.place(anchor="nw", relx=0.55, rely=0.27, x=0, y=0)
        self.ent_R2.bind("<FocusIn>", lambda e:self.ent_R2.delete("0","end"))
        self.ent_R3 = ttk.Entry(self.frame2)
        self.ent_R3.configure(width=10)
        _text_ = 'R3'
        self.ent_R3.delete("0", "end")
        self.ent_R3.insert("0", _text_)
        self.ent_R3.place(anchor="nw", relx=0.75, rely=0.36, x=0, y=0)
        self.ent_R3.bind("<FocusIn>", lambda e:self.ent_R3.delete("0","end"))
        self.frame2.pack(side="top")
        self.add(self.frame2, weight="1")
        self.frame3 = ttk.Frame(self)
        self.frame3.configure(height=50, width=600)
        self.frame6 = ttk.Frame(self.frame3)
        self.frame6.configure(height=50, relief="groove")
        self.rbtn_ds = ttk.Radiobutton(self.frame6)
        self.conv_var = tk.IntVar(value=1)
        self.rbtn_ds.configure(
            cursor="hand2",
            text='Delta-Star',
            value=1,
            variable=self.conv_var)
        self.rbtn_ds.pack(anchor="center", padx=15, side="left")
        self.rbtn_ds.configure(command=self.delta_star_adjust)
        self.rbtn_sd = ttk.Radiobutton(self.frame6)
        self.rbtn_sd.configure(
            cursor="hand2",
            text='Star-Delta',
            value=2,
            variable=self.conv_var)
        self.rbtn_sd.pack(anchor="center", padx=15, side="left")
        self.rbtn_sd.configure(command=self.delta_star_adjust)
        self.frame6.pack(
            expand="true",
            fill="both",
            padx=10,
            pady=10,
            side="left")
        self.frame7 = ttk.Frame(self.frame3)
        self.frame7.configure(height=50, width=200)
        self.btn_calc = ttk.Button(self.frame7)
        self.btn_calc.configure(cursor="hand2", text='Calculate')
        self.btn_calc.pack(anchor="center", padx=20, pady=30, side="right")
        self.btn_calc.configure(command=self.delta_star_con)
        self.frame7.pack(
            expand="true",
            fill="both",
            padx=10,
            pady=10,
            side="left")
        self.frame3.pack(side="top")
        self.add(self.frame3, weight="1")
        self.configure(height=500, width=600)
        self.pack(side="top")

    def lamda(self, event=None):
        pass

    def callback(self, event=None):
        pass

    def delta_star_adjust(self):
        pass

    def delta_star_con(self):
        pass
