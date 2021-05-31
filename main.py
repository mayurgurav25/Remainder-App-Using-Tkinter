
import tkinter as tk
from PIL import Image, ImageTk
import time
from plyer import notification
root = tk.Tk()
Canvas = tk.Canvas(root, width=1250, height=300)
Canvas.grid(columnspan=6)
root.title("Reminder App Using Tkinter")
timer =tk.Entry(root)
timer.grid(column=1, row=0)

messege =tk.Entry(root)
messege.grid(column=3, row=0)

noft=tk.Entry(root)
noft.grid(column=5, row=0)


logo = Image.open('logo1.png')
logo = ImageTk.PhotoImage(logo)
logo_label1 = tk.Label(image=logo)
logo_label1.image = logo
logo_label1.grid(column=0, row=0)
Canvas.grid(column =0)

instructions = tk.Label(root, text="**This Application will send you notification with a messege in certain interval**", fg="red")
instructions.grid(columnspan=3, column = 0, row=1 )
instructions = tk.Label(root, text="Now Set All Your Remainders Very Easily", font="Raleway")
instructions.grid(columnspan=3, column = 0, row=5 )
instructions1 = tk.Label(root, text="Set your timer")
instructions1.grid(columnspan=3, column = 0, row=0 )
instructions2 = tk.Label(root, text="Enter Messege for Notification")
instructions2.grid(columnspan=3, column =1, row=0 )
instructions3= tk.Label(root, text="Enter no. of Notification")
instructions3.grid(columnspan=3, column =3, row=0 )


def myClick():
	timer1 = int(timer.get())
	noft1 = int(noft.get())
	messege1 = str(messege.get())

	if __name__ == '__main__':
		for i in range(noft1):
			time.sleep(timer1)
			notification.notify(
				title="Remainder",
				message=messege1,
				app_icon="icon.ico",
				timeout=10
			)





def close():
    root.quit()




browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable= browse_text, height = 2,width = 15,fg="white", bg="blue", command=myClick)
browse_text.set("Set Remainder")
browse_btn.grid(column=4, row=1)

browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable= browse_text, height = 2,width = 15,fg="black", bg="yellow", command=close)
browse_text.set("Close")
browse_btn.grid(column=5, row=1)

root.mainloop()










