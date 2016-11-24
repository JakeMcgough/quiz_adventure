#to restart the game if you get an answer wrong come back on this and press f5
import time

direction = " "
health = 10


def health_bar():
    #put this before every thing
    
    print("===================")
    print("HP:", health)
    print("===================")
    print("")

def room1():

    health_bar()
    global health
    
    print("You have three options of rooms")
    print("You can go left, right or straight forward")
    print("l.left")
    print("r.right")
    print("s.straight forward")
    direction = input ("Direction ")
    print(direction)

    if direction.lower() == "l":
        left_room()

    if direction.lower() == "s":
        straightforward_room()

    if direction.lower() == "r":
        room2()    

def left_room():

    health_bar()
    global health 
    print("You go through the door")
    print("You notice the door shuts behind you")
    print("You have two options")
    print("a.jump into the bottomless pit to start again")
    print("b.jump through the many obsticles and back to get a key to get out")
    direction = input ("Direction ")
    print(direction)

    if direction.lower() == "a":
          print("You have died")
          print("Restarting...")
          time.sleep(5)
          room1()

    if direction.lower() == "b":
          print("You have got back")
          print("You are now back in room1 and get another chance to choose")
          import time
          time.sleep(5)
          room1()

def straightforward_room():

    health_bar()
    global health 
    print("You go through the wrong room")
    print("The door gets locked")
    print("You see a giant monster and realise you're in the wrong room")
    print("You can either...")
    print("a.accept your fate and let the moster eat you")
    print("b.fight the monster and get back out the room")
    direction = input ("Direction ")
    print(direction)

    if direction.lower() == "a":
        print("You are now dead")
        print("You are now back to room1")
        print("Restarting...")
        time.sleep(5)
        room1()

    if direction.lower() == "b":
        print("You have killed the monster and have collected the key")
        print("You are now back in room1 and get another chance to choose")
        time.sleep(5)
        room1()

def room2():

    health_bar()
    global health 

    print("You have chose the right room")
    print("You now have two options...")
    print("a.go right and do the many jumps over the treaturious bottomless pit with apples at the bottom")
    print("b.go left through the mystery door and find a key")
    direction = input ("Direction ")
    print(direction)

    if direction.lower() == "a":
        print("You made it to the last jump but you have met a dead end")
        print("You are now dead")
        print("Restarting...")
        import time
        time.sleep(5)
        room1()

    elif direction.lower() == "b":
        print("You have chose the right door")
        print("You go through the door to room3")
        room3()
        

def room3():

    health_bar()
    global health 

    print("You go through the door and find a 3 headed dog named fluffy")
    print("You have two options")
    print("a. Befriend fluffy and nicely ask for the key to room3")
    print("b. Attempt to kill fluffy and get the key by force")
    direction = input ("Direction ")
    print(direction)

    if direction.lower() == "a":
        print("You have retrieved the key and can now pass through to room4")
        room4()

    elif direction.lower() == "b":
        print("You have chosen the wrong day to mess with fluffy and fluffy has shread you to pieces")
        print("You have been sent back to room2")
        import time
        time.sleep(5)
        room2()

def room4():

    health_bar()
    global health 

    print("You walk into room4 and see another three headed beast")
    print("However this time it's a giant three headed dragon")
    print("You need to fight it to get the key for the next room")
    print("a. slice the neck of the main dragon")
    print("b. slice the neck of the left dragon")
    print("c. slice the neck of the right dragon")
    direction = input ("Direction ")
    print(direction)

    if direction.lower() == "a":
        print("You hit the wrong head you have lost -1 health")
        health = health -1
        print("You are now knocked back to room3")
        time.sleep(5)
        room3()

    elif direction == "b":
        print("You have killed the correct head and can now pass through")
        room5()

    elif direction == "c":
        print("You have hit the wrong head")
        health = health -2
        print("You have been knocked back to room3")
        time.sleep(5)
        room3()


def room5():

    health_bar()
    global health

    print("You are now faced with a maze")
    print("there are three ways to go")
    print("a. go left")
    print("b. go right")
    print("c. go down the ladder")
    direction = input ("Direction ")
    print(direction)

    if direction.lower() == "a":
        print("You have ran right into a trap of spikes")
        health = health -1
        print("You are now knocked back to room4")
        time.sleep(5)
        room4()

    elif direction.lower() == "b":
        print("You have chose the wrong path you have to run back to room5 before the the giant gorilla gets you")
        room5()

    elif direction.lower() == "c":
        print("You have chose the right option to go down the ladder well done")
        room6()


def room6():

    health_bar()
    global health

    

    
         

    
        
        
        

    

   
        

          
          
          

          

          
          

          

          

              

          

              
    

















# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()

    
