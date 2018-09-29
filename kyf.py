#import twisted # TCP connections
#import pytest  # Testing playground
import json
import threading # multithread support
#import getNames # webSocket Support
from queue import Queue # queue support
import talker
import time
import socketserver


class game():

    dataQueue = Queue()

    def build():
        game = playground()

    def rcvCommand(self,info):

        print(info)
        self.dataQueue.put(info)
        self.dataQueue.task_done()
        print(self.dataQueue.qsize())

    def socketSetup(self):
        talker.startTCP(self)

class playground():

    day = 1
    phase = True   # True = Day and False = Night


    def advance(): ## Advances to the next time slot
        if(phase == False):
            day += 1

        phase = not phase

class player():

    Name = []
    Role = "Villager"
    hit = False
    saved = False
    votes = 0

    #def kill(id, who):

if __name__ == '__main__':

    mafiaGame = game()

    threads = []
    t = threading.Thread(target=mafiaGame.socketSetup)
    threads.append(t)
    t.start()


    while(True):
        time.sleep(2)
        print('Main thread is here!   ' + str(mafiaGame.dataQueue.qsize()))
        #if dataQueue.empty() == False:
            #print(dataQueue.get())




    # number_of_players = 7
    # ## Game setup
    # participants = [player()] * number_of_players
    #
    # for x in range(participants):
    #     participants[x].Name = playerNames[X]
    #     print(participants[x].Name)
