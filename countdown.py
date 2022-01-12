import tkinter as tk

print("Xs for seconds, Xm for minutes, Xh for hours... i.e.: 1h50m")
c = input("Countdown length: ")
counter = 0
ll=0

for i in range(0, len(c)):
    if c[i] == "s":
        counter += int(c[ll:i])
        ll=i+1
    if c[i] == "m":
        counter += int(c[ll:i])*60
        ll=i+1
    if c[i] == "h":
        counter += int(c[ll:i])*3600
        ll=i+1

def counter_label(label1, label2, label3):
    def count():
        global counter
        counter -= 1
        label3.config(text=str(counter%60)+"s")
        label3.after(1000, count)
        label2.config(text=str(counter//60%60)+"m:")
        label1.config(text=str(counter//60//60%24)+"h:")
    count()
root = tk.Tk()
root.title("SpeedRun Counter")
root.configure(bg="black")
root.geometry("370x60")
#root.resizable(False,False)
label1 = tk.Label(root, fg="white", width="3", bg="black", font="Arial 32 bold")
label1.pack(side="left")
label2 = tk.Label(root, fg="white", width="4", bg="black", font="Arial 32 bold")
label2.pack(side="left")
label3 = tk.Label(root, fg="white", width="3", bg="black", font="Arial 32 bold")
label3.pack(side="left")
counter_label(label1, label2, label3)
button = tk.Button(root, text='Stop', fg="white", bg="black", font="Arial 20 bold", command=root.destroy)
button.pack(side="left")
root.mainloop()


