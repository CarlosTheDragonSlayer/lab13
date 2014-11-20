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
player = drawpad.create_rectangle(390,580,410,600, fill="red")
directionE = 1
directionZ = 1
directionD = 1

# Create your "enemies" here, before the class
enemyOne = drawpad.create_oval(50,50,119,188, fill="purple")
enemyTwo = drawpad.create_oval(50,200,188,269, fill="blue")
enemyThree = drawpad.create_oval(50,300,188,438, fill="green")

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="Up", background= "red")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "red")
       	    self.down.grid(row=2,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "red")
       	    self.left.grid(row=1,column=0)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "red")
       	    self.right.grid(row=1,column=2)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    
       	def upClicked(self, event):   
	    global oval
	    global player
	    drawpad.move(player,0,-20)
	   
	def downClicked(self, event):   
	    global oval
	    global player
	    drawpad.move(player,0,20)
	   
	def leftClicked(self, event):   
	    global oval
	    global player
	    drawpad.move(player,-20,0)
	   
	def rightClicked(self, event):   
	    global oval
	    global player
	    drawpad.move(player,20,0)
	
def animateE():
	global drawpad
	global player
	global enemyOne
	global enemyTwo
	global enemyThree
	global directionE
	# Remember to include your "enemies" with "global"
	Ex1, Ey1, Ex2, Ey2 = drawpad.coords(enemyOne)
        if Ex2 > int(drawpad.winfo_width())+69: 
            directionE = -869
        elif Ex1 < 0:
            directionE = 690
        drawpad.move(enemyOne,directionE,0)
        drawpad.after(20,animateE)
            
def animateZ():
	global drawpad
	global player
	global enemyOne
	global enemyTwo
	global enemyThree
	global directionZ
        Zx1, Zy1, Zx2, Zy2 = drawpad.coords(enemyTwo)
        if Zx2 > int(drawpad.winfo_width())+138: 
            directionZ = -938
        elif Zx1 < 0:
            directionZ = 69
        drawpad.move(enemyTwo,directionZ,0)
        drawpad.after(20,animateZ)
            	    
def animateD():
	global drawpad
	global player
	global enemyOne
	global enemyTwo
	global enemyThree
	global directionD
        Dx1, Dy1, Dx2, Dy2 = drawpad.coords(enemyThree)
        if Dx2 > int(drawpad.winfo_width())+138: 
            directionD = -938
        elif Dx1 < 0:
            directionD = 6.9
        drawpad.move(enemyThree,directionD,0)
	drawpad.after(20,animateD)
		
# call the animate function to start our recursion
animateE()
animateZ()
animateD()

app = MyApp(root)
root.mainloop()