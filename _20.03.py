from tkinter import * 
raam=Tk()
raam.title("Tahvel")
tahvel=Canvas(raam, width=600, height=600, background="pink")
tahvel.grid()
#monako
tahvel.create_rectangle(30,50,300,300,fill="white")
tahvel.create_rectangle(30,300,300,400,fill="red")

#estonia
tahvel.create_rectangle(500,50, 260,150,fill="blue")
tahvel.create_rectangle(500,100, 260,150,fill="black")
tahvel.create_rectangle(500,200, 260,150,fill="white")

#bahama
tahvel.create_rectangle(25,50, 250,150,fill="cyan")
tahvel.create_rectangle(25,100, 250,150,fill="yellow")
tahvel.create_rectangle(25,200, 250,150,fill="cyan")

tahvel.create_polygon(25,50,110,125,25,200, fill="black")

raam.mainloop()