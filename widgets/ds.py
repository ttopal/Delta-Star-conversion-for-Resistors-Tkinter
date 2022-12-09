# Delta-Star Conversion
import tkinter as tk
import tkinter.ttk as ttk

# internals
from .ds_widget import DeltaStarWidget

class DeltaStar(DeltaStarWidget):
    def __init__(self, *args, **kwargs):
        DeltaStarWidget.__init__(self, *args, **kwargs)

        self.img = tk.PhotoImage(file="DS_con1.png")
        self.cn_entry.create_image(0, 0, image=self.img, anchor="nw")

        self.ent_Ra.place(anchor="nw", relx=0.42, rely=0.42, x=0, y=0)
        self.ent_Rb.place(anchor="nw", relx=0.65, rely=0.42, x=0, y=0)
        self.ent_Rc.place(anchor="nw", relx=0.6, rely=0.20, x=0, y=0)
        self.ent_R1.place(anchor="nw", relx=0.14, rely=0.62, x=0, y=0)
        self.ent_R2.place(anchor="nw", relx=0.01, rely=0.29, x=0, y=0)
        self.ent_R3.place(anchor="nw", relx=0.27, rely=0.29, x=0, y=0)
        
        # self.ent_Ra.bind("<FocusIn>", lambda e:self.ent_Ra.delete("0","end"))
        # self.ent_Rb.bind("<FocusIn>", lambda e:self.ent_Rb.delete("0","end"))
        # self.ent_Rc.bind("<FocusIn>", lambda e:self.ent_Rc.delete("0","end"))
        # self.ent_R1.bind("<FocusIn>", lambda e:self.ent_R1.delete("0","end"))
        # self.ent_R2.bind("<FocusIn>", lambda e:self.ent_R2.delete("0","end"))
        # self.ent_R3.bind("<FocusIn>", lambda e:self.ent_R3.delete("0","end"))

        self.Ra = tk.DoubleVar()
        self.ent_Ra.config(textvariable=self.Ra)
        self.Rb = tk.DoubleVar()
        self.ent_Rb.config(textvariable=self.Rb)
        self.Rc = tk.DoubleVar()
        self.ent_Rc.config(textvariable=self.Rc)

        self.R1 = tk.DoubleVar()
        self.ent_R1.config(textvariable=self.R1)
        self.R2 = tk.DoubleVar()
        self.ent_R2.config(textvariable=self.R2)
        self.R3 = tk.DoubleVar()
        self.ent_R3.config(textvariable=self.R3)
        self.delta_star_adjust()


    def delta_star_adjust(self):
        val = self.conv_var.get()
        if val == 1: # Delta-Star (1) Ra Rb Rc disable
            self.label2.configure(foreground="#00ff00")
            self.label3.configure(foreground="#008000")
            self.ent_Ra.config(state="disabled")
            self.ent_Rb.config(state="disabled")
            self.ent_Rc.config(state="disabled")
            self.ent_R1.config(state="")
            self.ent_R2.config(state="")
            self.ent_R3.config(state="")
            self.ent_R1.delete("0", "end")
            self.ent_R1.insert("0", "1")
            self.ent_R2.delete("0", "end")
            self.ent_R2.insert("0", "1")
            self.ent_R3.delete("0", "end")
            self.ent_R3.insert("0", "1")
                    
        else:  # Star-Delta (2)  R1 R2 R3 disable
            self.label3.configure(foreground="#00ff00")
            self.label2.configure(foreground="#008000")
            self.ent_Ra.config(state="")
            self.ent_Rb.config(state="")
            self.ent_Rc.config(state="")
            self.ent_R1.config(state="disabled")
            self.ent_R2.config(state="disabled")
            self.ent_R3.config(state="disabled")
            self.ent_Ra.delete("0", "end")
            self.ent_Ra.insert("0", "1")
            self.ent_Rb.delete("0", "end")
            self.ent_Rb.insert("0", "1")
            self.ent_Rc.delete("0", "end")
            self.ent_Rc.insert("0", "1")
            

    def delta_star_con(self):
        val = self.conv_var.get()
        if val == 1: # Delta-Star (1) Ra Rb Rc disable
            val_R1 = self.R1.get()
            val_R2 = self.R2.get()
            val_R3 = self.R3.get()
            val_Rt = val_R1 + val_R2 + val_R3
            val_Ra = val_R1 * val_R2 / val_Rt
            val_Rb = val_R1 * val_R3 / val_Rt
            val_Rc = val_R2 * val_R3 / val_Rt
            self.Ra.set(f"{val_Ra:5.2f}")
            self.Rb.set(f"{val_Rb:5.2f}")
            self.Rc.set(f"{val_Rc:5.2f}")

        else:  # Star-Delta (2)  R1 R2 R3 disable
            val_Ra = self.Ra.get()
            val_Rb = self.Rb.get()
            val_Rc = self.Rc.get()
            val_Rmt = val_Ra * val_Rb + val_Ra * val_Rc + val_Rb * val_Rc
            val_R1 = val_Rmt / val_Rc
            val_R2 = val_Rmt / val_Rb
            val_R3 = val_Rmt / val_Ra
            self.R1.set(f"{val_R1:5.2f}")
            self.R2.set(f"{val_R2:5.2f}")
            self.R3.set(f"{val_R3:5.2f}")