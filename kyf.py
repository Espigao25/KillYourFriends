#import twisted # TCP connections
#import pytest  # Testing playground
import json
import threading # multithread support
#import getNames # webSocket Support
from queue import Queue # queue support
import talker, listener, speaker
import time
import sys
import random
import socketserver


class Game:

    def __init__(self):
        self.dataQueue = Queue()
        self.outgoingQueue = Queue()


    def build(self, playerList):

        random.shuffle(playerList)
        self.village = self.Village(playerList)

    def rcvCommand(self,info):

        self.dataQueue.put(info)
        self.dataQueue.task_done()

    def socketSetup(self):
        speaker.startTCP(self)

    # def socketSetup_snd(self):
    #     talker.startTCP(self)

    class Village:

        def __init__(self, playerList):
            self.Village_NameList = []
            self.Village_People = []  # Array with all the people in the game
            self.professions=['Villager','Villager','Villager','Policeman', 'Doctor', 'Mafia', 'Mafia']
            for x in range(len(playerList)):
                self.Village_NameList.append(playerList[x])   # adiciona o nome à lista
                self.Village_People.append(self.Player(playerList[x], self.professions[x]))   # cria a classe e junta á lista


        day = 1
        phase = True   # True = Day and False = Night


        def advance(): ## Advances to the next time slot
            if(phase == False):
                day += 1

            phase = not phase

        class Player:

            def __init__(self, name, role):

                self.Name = name
                self.Team = 0   # 0 = village  ||||    1 = Mafia
                self.Role = role
                self.alive = True
                self.hit = False
                self.protected = False
                self.visitedBy = []

            #def kill(id, who):

if __name__ == '__main__':

    mafiaGame = Game()

    threads = []
    parallel_functions = [mafiaGame.socketSetup]
    for x in range(len(parallel_functions)):
        t = threading.Thread(target=parallel_functions[x])
        threads.append(t)
        t.start()



    while(True):
        time.sleep(1)

        print('\r Main thread is here!   Incoming: ' + str(mafiaGame.dataQueue.qsize()) + '   Outgoing: ' + str(mafiaGame.outgoingQueue.qsize()) ,end = '' )

        mafiaGame.outgoingQueue.put('HEARTBEAT,' + str(time.time()))
        if mafiaGame.dataQueue.empty() == False:
            print(str(mafiaGame.dataQueue.get()))
            #mafiaGame.build(mafiaGame.dataQueue.get())

    time.sleep(3)

    for x in range(len(mafiaGame.village.Village_People)):
        print(vars(mafiaGame.village.Village_People[x]))

    # number_of_players = 7
    # ## Game setup
    # participants = [player()] * number_of_players
    #
    # for x in range(participants):
    #     participants[x].Name = playerNames[X]
    #     print(participants[x].Name)
