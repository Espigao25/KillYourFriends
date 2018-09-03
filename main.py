import tkinter as tk
import time


frame = tk.Tk()
frame.title("KillYourFriends 0.1")
frame.geometry("530x700+30+30")

## Initializations of Variables


playerNumber = 15

playerList = [tk.StringVar() for x in range(playerNumber)]

n = 1
for player in playerList:
    player.set("Placeholder" + str(n))
    n += 1


## Initialization of functions
    
def gameStart():
    gameSetup = 0
    return gameSetup


## Initializations of GUI


title = tk.Label(frame,
                    text="Game Setup",
                    justify = tk.RIGHT,
                    font = "Arial 18 bold",
                    pady=25)

blankspace = tk.Label(frame,
                     text="    ",
                     justify = tk.CENTER,
                     pady = 10)

roles = tk.Label(frame,
                     text="In-game roles",
                     font = "Arial 14 bold",
                     justify = tk.RIGHT,
                     pady = 10)

vil_label = tk.Label(frame,
                     text="Villagers:",
                     justify = tk.RIGHT,
                     width = 20,
                     pady=10)

doc_label = tk.Label(frame,
                     text="Doctors:",
                     justify = tk.CENTER,
                     pady=10)

cop_label = tk.Label(frame,
                     text="Policemen:",
                     justify = tk.CENTER,
                     pady=10)

Maf_label = tk.Label(frame,
                     text="Mafias:",
                     justify = tk.CENTER,
                     pady=10)

vil_entry = tk.Entry(frame, width = 2)
doc_entry = tk.Entry(frame, width = 2)
cop_entry = tk.Entry(frame, width = 2)
Maf_entry = tk.Entry(frame, width = 2)


lobby = tk.Label(frame,
                     text="Player Lobby",
                     justify = tk.RIGHT,
                     font = "Arial 14 bold",
                     pady = 10)


startBtn = tk.Button(frame, text='Start the Game', width=10, command=gameStart)

quitBtn = tk.Button(frame, text='Quit', width=10, command=frame.destroy)


## Placements

def setupRefresh():

    blankspace.grid(row = 3, column = 1)    

    title.grid(row = 1, column = 6)

    roles.grid (row = 3, column = 2)

    vil_label.grid(row = 4, column = 2)
    doc_label.grid(row = 5, column = 2)
    cop_label.grid(row = 6, column = 2)
    Maf_label.grid(row = 7, column = 2)

    vil_entry.grid(row = 4, column = 3)
    doc_entry.grid(row = 5, column = 3)
    cop_entry.grid(row = 6, column = 3)
    Maf_entry.grid(row = 7, column = 3)

    blankspace.grid(row = 3, column = 4)
    blankspace.grid(row = 3, column = 5)

    lobby.grid(row = 3, column = 6)

    n = 4
    for slot in playerList:
        tk.Label(frame, text=slot.get(), pady = 10).grid(row = n, column = 6)
        n +=1
        
        
    startBtn.grid(row = n-2, column = 8)
    quitBtn.grid(row = n-1, column = 8)
      


while True:

    setupRefresh()
    time.sleep(2)

frame.mainloop()