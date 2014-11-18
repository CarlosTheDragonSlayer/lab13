#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="green")
enemy1 = drawpad.create_rectangle(50,100,70,20, fill="red")
enemy2 = drawpad.create_rectangle(390,250,410,270, fill="red")
enemy3 = drawpad.create_rectangle(780,400,800,420, fill="red")

direction = 5
direction2 = 7
direction3 = -9


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    self.up.bind("<Button-1>", self.upClicked)
    
       	    drawpad.pack(side=BOTTOM)
       	    
       	    self.bottom = Button(self.myContainer1)
       	    self.bottom.configure(text="bottom", background= "blue")
       	    self.bottom.grid(row=2,column=1)
       	    self.bottom.bind("<Button-1>", self.downClicked)
    
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    #drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
        def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)	

app = MyApp(root)
root.mainloop()