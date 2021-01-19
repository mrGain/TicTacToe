# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:31:10 2020

@author: RAKESH
"""

import numpy
board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
#print(board)
p1s='X'
p2s='O'


def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
            if count==3 :
                print(symbol,"own")
                return True
    return  False  

def check_column(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
            if count==3 :
                print(symbol,"own")
                return True
    return  False       

def check_digonal(symbol):
    if board[0][2] == board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol,"own")
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board==symbol:
        print(symbol,"own")
        return True
    return False

def own(symbol):
    return check_rows(symbol) or check_column(symbol) or check_digonal(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("Enter row 1 or 2 or 3 : "))
        col=int(input("Enter column 1 or 2 or 3 : "))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='_':
            break
        else:
            print("Invalid Input ,please enter again.")
    board[row-1][col-1]=symbol        
    
    
def play():
    for turn in range(9):
        if(turn%2 == 0):
            print(" X It's Your turn")
            place(p1s)
            if own(p1s):
                break
        else:
            print(" O It's Your turn")
            place(p2s)
            if own(p2s):
                break
    if not(own(p1s)) and not(own(p2s)):
        print("Draw")

play()