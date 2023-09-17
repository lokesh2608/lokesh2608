import tkinter as tk
r=tk.tk()
r.tittle('counting seconds')
button= tk.Button(r, text='stop',width=25,command=r.destroy)
button.pack()
r.mainloop()