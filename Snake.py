'''
  Snake Game Using Python tkinter
  Hello World ! I am Pratik Rathod 
    A snake game experiment in just 4 hours
'''

from tkinter import *
import random
import tkinter.messagebox as tkbox


class Snake:
    def __init__(self, root=None):
        '''Globles Variables'''
        self.root = root
        #Height & Width
        self.windowWidth = 895
        self.windowHeight = 495
        self.score = 0
        
        # gameBoundary
        self.gameBoundaryTop = 20
        self.gameBoundaryBottom = self.windowHeight-20
        self.gameBoundaryRight = self.windowWidth-20
        self.gameBoundaryLeft = 20

        #direction
        self.direction = "Right"
        # snakeIntialCordinates
        self.steps = 20
        self.speed = 120 # ms
        self.x = 0
        self.y = self.steps
        
        # virtual coordnates
        self.xpos_snake = 6
        self.ypos_snake = 5

        self.x0 = self.steps * (self.xpos_snake+1)
        self.y0 = self.steps * (self.ypos_snake+1)

        # food
        self.food = None
        
        #snake
        snake = [[self.xpos_snake,self.ypos_snake] for x in range(1,4)]
        
        # canvas variable
        self.c = Canvas(self.root, bg="black", height=int(
        self.root.winfo_screenheight()-200), width=self.root.winfo_screenwidth())
        self.c.pack()

        # calling Window function
        player = self.snakePlayer(snake)
        self.snakeWindow()
        self.design()
        self.scoreLable = self.c.create_text(770,450,fill="gray",font="Times 18",text="Score : 0")
        self.movePlayer(snake,player)
        
    def snakeWindow(self):
        # Gets both half the screen width/height and window width/height
        positionRight = int(
            self.root.winfo_screenwidth()/2 - self.windowWidth/2)
        positionDown = int(
            self.root.winfo_screenheight()/2 - self.windowHeight/2)
        # Positions the window in the center of the page.
        self.root.geometry("{}x{}+{}+{}".format(self.windowWidth,
                                                self.windowHeight, positionRight, positionDown))
        self.c.create_text(150,40,fill="darkblue",font="Castellar 18 italic bold",text=" A snake Game")
    def design(self):
        # Top Boudary
        self.c.create_rectangle(
            0, 0, self.windowWidth, self.gameBoundaryTop, fill="gray", outline="gray")
        self.c.create_text(100,10,fill="lightgray",font="Times 12 ",text="Creator : Pratik Rathod")
        # Bottom Boundary
        self.c.create_rectangle(0, self.windowHeight, self.windowWidth,
                                self.gameBoundaryBottom, fill="gray", outline="gray")
        # Left Boundary
        self.c.create_rectangle(0, 0, self.gameBoundaryLeft,
                                self.windowHeight, fill="gray", outline="gray")
        # Right Boundary
        self.c.create_rectangle(self.windowWidth, 0, self.gameBoundaryRight,
                                self.windowHeight, fill="gray", outline="gray")

    def snakePlayer(self,snake):
        player = []
        for x,y in snake:
            self.x0 = self.steps * x
            self.y0 = self.steps * y

            ract = self.c.create_rectangle(
             self.x0, self.y0, self.x0+15, self.y0+15, fill="brown", outline="red")
            player.append(ract)
        return player

    def createFood(self):
        self.c.itemconfigure(self.scoreLable,text="Score : "+str(self.score))
        self.xpos = random.randrange(20, self.gameBoundaryRight-90, 20)
        self.ypos = random.randrange(20, self.gameBoundaryBottom, 20)
        self.food = self.c.create_rectangle(
            self.xpos, self.ypos, self.xpos+15, self.ypos+15, fill="yellow", outline="yellow")

    def movePlayer(self,snake,player,delete_tail=True):
        
        self.c.move(player, self.x, self.y)
         # get head
        x, y = snake[0]
        direction = self.direction
        
        if direction == 'Up':
            y = y-1
        elif direction == 'Down':
            y = y+1
        elif direction == 'Left':
            x = x-1
        elif direction == 'Right':
            x = x+1
       
        snake.insert(0, [x, y])
        
        self.x0 = self.steps * x
        self.y0 = self.steps * y

        ract = self.c.create_rectangle(
             self.x0, self.y0, self.x0+15, self.y0+15, fill="brown", outline="brown")
        player.insert(0,ract)

        if delete_tail :
            del snake[-1]
            self.c.delete(player[-1])
            del player[-1]
        
        if(self.food == None):
            self.createFood()
            
        if(self.c.coords(player[0]) == self.c.coords(self.food)):
            self.c.delete(self.food)
            self.score = self.score + 50
            self.food = None
            delete_tail = False
        else:
            delete_tail = True
        try:
            self.checkGameStatus(self.c.coords(player[0]))
            self.checkGameCollisions(player)
            self.c.after(self.speed, self.movePlayer,snake,player,delete_tail)
        except:
            print("Bye");    

    def checkGameStatus(self, snakeCordinates):
        if snakeCordinates[0] < self.gameBoundaryLeft:
            tkbox.showinfo("Shanke Says","Game Over \n Final Score :"+str(self.score))
            self.root.destroy()

        elif snakeCordinates[1] < self.gameBoundaryTop:
            tkbox.showinfo("Shanke Says","Game Over \n Final Score :"+str(self.score))
            self.root.destroy()

        elif snakeCordinates[2] > self.gameBoundaryRight:
            tkbox.showinfo("Shanke Says","Game Over \n Final Score :"+str(self.score))
            self.root.destroy()
            
        elif snakeCordinates[3] > self.gameBoundaryBottom:
            tkbox.showinfo("Shanke Says","Game Over \n Final Score :"+str(self.score))
            self.root.destroy()

    def checkGameCollisions(self,player):
        
        head = player[0] 

        self.c.coords(head)
        for i in range(1,len(player)):
            if(self.c.coords(head) == self.c.coords(player[i])):
                tkbox.showinfo("Shanke Says","Game Over \n Final Score :"+str(self.score))
                self.root.destroy()

    def control(self, event):
        if event.keysym == 'Escape':
            print("Bye")
            self.root.destroy()
        if event.keysym == 'Up':
            if self.direction !='Down':
                self.direction = event.keysym
        if event.keysym == 'Down':
            if self.direction !='Up':
                self.direction = event.keysym
        if event.keysym == 'Left':
            if self.direction !='Right':
                self.direction = event.keysym
        if event.keysym == 'Right':
            if self.direction !='Left':
                self.direction = event.keysym
        if event.keysym == 'space':
            if self.steps < 20:
                self.steps = self.steps+1
            print(self.steps)
        elif event.keysym == 'Shift_L':
            if self.steps > 5:
                self.steps = self.steps-1
            print(self.steps)
        if event.keysym == 'comma':
            if(self.speed > 10):
                self.speed = self.speed-10
            print(self.speed)
        elif event.keysym == 'period':
            if(self.speed < 1000):
                self.speed = self.speed+10
            print(self.speed)


# Function
if __name__ == "__main__":
    # root variable
    root = Tk()
    root.overrideredirect(1)
    snake = Snake(root)
    # Keys Events
    root.bind_all('<Key>', snake.control)
    mainloop()
