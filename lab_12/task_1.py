import tkinter as tk
from tkinter import ttk, messagebox

class CGPA(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CGPA management system")
        '''
        self.courses = []
        self.courses.append(("OOP",3))
        self.courses.append(("OOP Lab",1))
        self.courses.append(("English",2))
        self.courses.append(("IST",2))
        '''
        full_window_frame = ttk.Frame(self)
        full_window_frame.grid(row=0, column=0, padx=10, pady=10)
        #oop
        self.oop_label = ttk.Label(full_window_frame, text="OOP")
        self.oop_label.grid(row=0, column=0, padx=10, pady=10)

        self.oop_marks = tk.IntVar()
        self.oop_entry = ttk.Entry(full_window_frame, width=30)
        self.oop_entry.grid(row=0, column=1, padx=10, pady=10)
        self.oop_entry["textvariable"] = self.oop_marks

        
        #oop lab
        self.ooplab_label = ttk.Label(full_window_frame, text="OOP LAB")
        self.ooplab_label.grid(row=1, column=0, padx=10, pady=10)

        self.ooplab_marks = tk.IntVar()
        self.ooplab_entry = ttk.Entry(full_window_frame, width=30)
        self.ooplab_entry.grid(row=1, column=1, padx=10, pady=10)
        self.ooplab_entry["textvariable"] = self.ooplab_marks

        
        #English
        self.eng_label = ttk.Label(full_window_frame, text="English")
        self.eng_label.grid(row=2, column=0, padx=10, pady=10)

        self.eng_marks = tk.IntVar()
        self.eng_entry = ttk.Entry(full_window_frame, width=30)
        self.eng_entry.grid(row=2, column=1, padx=10, pady=10)
        self.eng_entry["textvariable"] = self.eng_marks

        #Islamiat
        self.isl_label = ttk.Label(full_window_frame, text="Islamiat")
        self.isl_label.grid(row=3, column=0, padx=10, pady=10)

        self.isl_marks = tk.IntVar()
        self.isl_entry = ttk.Entry(full_window_frame, width=30)
        self.isl_entry.grid(row=3, column=1, padx=10, pady=10)
        self.isl_entry["textvariable"] = self.isl_marks

        self.cgpa_cal_button = ttk.Button(full_window_frame, text="Calculate CGPA")
        self.cgpa_cal_button.grid(row=4, column=0, padx=10, pady=10)
        self.cgpa_cal_button.bind('<Button-1>', self.cal_cgpa)


    def cal_cgpa(self, event):
        self.oop_marks=self.oop_marks.get()
        self.ooplab_marks=self.ooplab_marks.get()
        self.eng_marks= self.eng_marks.get()
        self.isl_marks= self.isl_marks.get()
        self.oop_marks = (self.oop_marks/100)*3
        self.ooplab_marks = (self.ooplab_marks/100)*1
        self.eng_marks = (self.eng_marks/100)*2
        self.isl_marks = (self.isl_marks/100)*2
        self.gpa = (self.oop_marks+self.ooplab_marks+ self.eng_marks+self.isl_marks)/8
        self.cgpa = self.gpa*4

        messagebox.showinfo(title="Your cgpa", message=f"cgpa is: {self.cgpa:.2f}")
 

def main():
    CGPA().mainloop()

main()   