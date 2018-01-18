import sys
import os

class ttToe:
    __tableTop = ''
    __tableMid = ''
    __tableBot = ''
    __tableSplit = ('-----------')
    __playGame = True

    def __init__(self):
        for t in range(0,3):
            self.__tableTop += ('    |   |   \n')
        self.__tableMid = self.__tableTop
        self.__tableBot = self.__tableTop

    def beginGame(self):
        char = 'X'
        while(self.__playGame):
            self.printTable()
            cont = input("Enter 'c' to continue or 'q' to quit\n")
            if cont == 'q':
                break
            level = int(input("Choose a level #: "))
            box = int(input("Choose a box #: "))
            self.insertC(level,box,char)
            if char == 'X':
                char = 'O'
            else:
                char = 'X'

    def printTable(self):
        print(' Tic Tac Toe \n' + self.__tableTop, self.__tableSplit, '\n' + self.__tableMid,
              self.__tableSplit, '\n' + self.__tableBot)

    def insertC(self, level, box, char):
        if level == 1:
            if box == 1:
                self.__tableTop = self.__tableTop[0:15] + char + self.__tableTop[16:]
            if box == 2:
                self.__tableTop = self.__tableTop[0:19] + char + self.__tableTop[20:]
            if box == 3:
                self.__tableTop = self.__tableTop[0:23] + char + self.__tableTop[24:]
        elif level == 2:
            if box == 1:
                self.__tableMid = self.__tableMid[0:15] + char + self.__tableMid[16:]
            if box == 2:
                self.__tableMid = self.__tableMid[0:19] + char + self.__tableMid[20:]
            if box == 3:
                self.__tableMid = self.__tableMid[0:23] + char + self.__tableMid[24:]
        else:
            if box == 1:
                self.__tableBot = self.__tableBot[0:15] + char + self.__tableBot[16:]
            if box == 2:
                self.__tableBot = self.__tableBot[0:19] + char + self.__tableBot[20:]
            if box == 3:
                self.__tableBot = self.__tableBot[0:23] + char + self.__tableBot[24:]

    
    

game = ttToe()
game.beginGame()
