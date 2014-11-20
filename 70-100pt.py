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
player = drawpad.create_oval(390,580,410,600, fill="red")
opponent = drawpad.create_rectangle(490,580,410,600, fill="red")
player = drawpad.create_rectangle(390,580,410,600, fill="blue")
 
 # Create your "enemies" here, before the class
def __init__(self, parent):
        	    # Bind an event to the first button
            self.up.bind("<Button-1>", self.upClicked)
        	    
      	    self.myParent = parent  
     	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="Down", background= "Blue")
       	    self.down.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "Red")
       	    self.right.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "purple")
       	    self.left.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
       	    drawpad.pack(side=BOTTOM)

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
	 
def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	
def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
		
		
app = MyApp(root)
root.mainloop()
root.mainloop()