import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

root = tk.CTk()
root.geometry("1920x1080")
root.state("zoomed")

_relative_row = 1
_relative_column = 1

def createTimeList(frame:tk.CTkFrame, payload:list):
    for i in range(114):
        payload.append(tk.CTkFrame(master=frame))
        payload[i].pack(in_=frame, expand=True, fill='both')
        payload[i].configure(height=10)


userInputFrame = tk.CTkFrame(master=root)
userInputFrame.grid(row=0 , column= 1)

monday = tk.CTkFrame(master=root)
monday.grid(row=_relative_row , column= _relative_column)

_mondayTimes = []
createTimeList(monday, _mondayTimes)
    

tuesday = tk.CTkFrame(master=root)
tuesday.grid(row=_relative_row , column= _relative_column+1)

wednesday = tk.CTkFrame(master=root)
wednesday.grid(row=_relative_row , column= _relative_column+2)

thursday = tk.CTkFrame(master=root)
thursday.grid(row=_relative_row , column= _relative_column+3)

friday = tk.CTkFrame(master=root)
friday.grid(row=_relative_row , column= _relative_column+4)

saturday = tk.CTkFrame(master=root)
saturday.grid(row=_relative_row , column= _relative_column+5)

sunday = tk.CTkFrame(master=root)
sunday.grid(row=_relative_row , column= _relative_column+6)




root.mainloop()