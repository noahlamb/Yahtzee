import tkinter as tk
from tkinter import *
from random import randint
from collections import Counter
games = [51,52,53,54,55,58,59,60,61,62]
p1tot = [-1,-1]
p2tot = [-1,-1]
gamecount = 0
check = 0
one,two,three,four,five,six = [-1], [-1], [-1], [-1], [-1], [-1]
one1,two1,three1,four1,five1,six1 = [-1], [-1], [-1], [-1], [-1], [-1]
one_cond,two_cond,three_cond,four_cond,five_cond,six_cond = [False],[False],[False],[False],[False],[False]
one_cond1,two_cond1,three_cond1,four_cond1,five_cond1,six_cond1 = [False],[False],[False],[False],[False],[False]
tkind_cond,fkind_cond,fhouse_cond,sstraight_cond,lstraight_cond,chance_cond = [False],[False],[False],[False],[False],[False]
tkind_cond1,fkind_cond1,fhouse_cond1,sstraight_cond1,lstraight_cond1,chance_cond1 = [False],[False],[False],[False],[False],[False]
last_cond = [False]
last_num = [0]
botcount,botcount2 = 0,0
botscore,botscore2 = 0,0
topcount = 0
loc1 = 1
loc2 = loc1+5
loc3 = loc2+5
loc4 = loc3+5
loc5 = loc4+5
loc6 = loc5+5
loc7 = loc6+5
val1 = True
val2 = True
val3 = True
val4 = True
val5 = True
val6 = True
rowval = 0
colval = 0
continued = False
continued2 = False
confirm = False
enlarge = 5
turn = True
scoreyat,scoreyat1 = -50,-50

def create_dice():
    """
    Creates the dice with all the sides drawn in a list.
    The sides are drawn by the draw_dice function.

    :return: dice list
    """
    dice = list()
    dice.append(draw_dice('dot0'))  # empty
    dice.append(draw_dice('dot4'))  # center dot --> 1
    dice.append(draw_dice('dot3', 'dot5'))  # dice head 2
    dice.append(draw_dice('dot2', 'dot4', 'dot6'))  # dice head 3
    dice.append(draw_dice('dot1', 'dot2', 'dot6', 'dot9'))  # dice head 4
    dice.append(draw_dice('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))  # dice head 5
    dice.append(draw_dice('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))  # dice head 6
    return dice


def draw_dice(*args):
    """
    Creates the individual heads passed in through the 
    create_dice function.

    :param args: string(s) for certain dots for certain heads
    :return: c canvas
    """
    w, h = 23*enlarge, 23*enlarge  # sets width and height
    x, y, r = 2*enlarge, 2*enlarge, 5*enlarge # sets x, y, and radius
    c = tk.Canvas(root, width=w, height=h, bg='white') # creates canvas c

    #Dictionary containing lambda functions to draw dots on canvas c
    dots = {
        'dot0': lambda x, y, r: c,
        'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
        'dot2': lambda x, y, r: c.create_oval(x + 16*enlarge, y, (x + 16*enlarge) + r, y + r, fill='black'),
        'dot3': lambda x, y, r: c.create_oval(x, y + 8*enlarge, x + r, (y + 8*enlarge) + r, fill='black'),
        'dot4': lambda x, y, r: c.create_oval(x + 8*enlarge, (y + 8*enlarge), (x + 8*enlarge) + r, (y + 8*enlarge) + r, fill='black'),
        'dot5': lambda x, y, r: c.create_oval(x + 16*enlarge, (y + 8*enlarge), (x + 16*enlarge) + r, (y + 8*enlarge) + r, fill='black'),
        'dot6': lambda x, y, r: c.create_oval(x, y + 16*enlarge, x + r, (y + 16*enlarge) + r, fill='black'),
        'dot9': lambda x, y, r: c.create_oval(x + 16*enlarge, y + 16*enlarge, (x + 16*enlarge) + r, (y + 16*enlarge) + r, fill='black')
    }

    for arg in args:
        dots.get(arg)(x, y, r) # Gets the dictionary keys while passing in x, y, and r values

    return c

def ngame():
    global gamecount,tkind_cond,tkind_cond1,fkind_cond1,fhouse_cond1,sstraight_cond1,lstraight_cond1,chance_cond1, one_cond1,two_cond1,three_cond1,four_cond1,five_cond1,six_cond1, p1tot,p2tot,continued, va1,val2,val3,val4,val5,val6, continued2, turn, games,one_cond,two_cond,three_cond,four_cond,five_cond,six_cond, one,two,three,four,five,six, one1,two1,three1,four1,five1,six1, botcount, botcount2, botscore,botscore2, topcountkind_cond,fkind_cond,fhouse_cond,sstraight_cond,lstraight_cond,chance_cond
    games = [51,52,53,54,55,58,59,60,61,62]
    p1tot = [-1,-1]
    p2tot = [-1,-1]
    one,two,three,four,five,six = [-1], [-1], [-1], [-1], [-1], [-1]
    one1,two1,three1,four1,five1,six1 = [-1], [-1], [-1], [-1], [-1], [-1]
    one_cond,two_cond,three_cond,four_cond,five_cond,six_cond = [False],[False],[False],[False],[False],[False]
    one_cond1,two_cond1,three_cond1,four_cond1,five_cond1,six_cond1 = [False],[False],[False],[False],[False],[False]
    tkind_cond,fkind_cond,fhouse_cond,sstraight_cond,lstraight_cond,chance_cond = [False],[False],[False],[False],[False],[False]
    tkind_cond1,fkind_cond1,fhouse_cond1,sstraight_cond1,lstraight_cond1,chance_cond1 = [False],[False],[False],[False],[False],[False]
    last_cond = [False]
    last_num = [0]
    botcount,botcount2 = 0,0
    botscore,botscore2 = 0,0
    topcount = 0
    continued = False
    continued2 = False
    confirm = False
    turn = True
    val1 = True
    val2 = True
    val3 = True
    val4 = True
    val5 = True
    val6 = True
    for i in [0,7]:
        L2 = tk.Label(root, text ="Game %d" % (gamecount+1), relief=SOLID)
        L2.grid(row = 2, column = games[gamecount]+i,sticky = NSEW)
        L3 = tk.Label(root, text ="Game %d" % (gamecount+2), relief=SOLID,bg = "green")
        L3.grid(row = 2, column = games[gamecount+1]+i,sticky = NSEW)
    gamecount += 1
    button11 = tk.Button(root, text="Next Game", command = ngame, state = "disabled")
    button11.grid(row=13, column=0)
    P1 = tk.Label(root, text="Player 1", fg='black',bg = 'yellow')
    P1.grid(row=1,column = 52)
    P2 = tk.Label(root, text="Player 2", fg='black', bg = 'white')
    P2.grid(row=1,column = 59)

def tot(score,i):
    global p1tot, p2tot
    if i < 56:
        if p1tot[0] == -1:
            p1tot[0] = score
        elif p1tot[1] == -1:
            p1tot[1] = score
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 20, column = i, sticky = NSEW)
            point = Label(root, text = str(sum(p1tot)), relief = SOLID)
            point.grid(row = 20, column = i, sticky = NSEW)
    if i > 56:
        if p2tot[0] == -1:
            p2tot[0] = score
        elif p2tot[1] == -1:
            p2tot[1] = score
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 20, column = i, sticky = NSEW)
            point = Label(root, text = str(sum(p2tot)), relief = SOLID)
            point.grid(row = 20, column = i, sticky = NSEW)
            button11 = tk.Button(root, text="Next Game", command = ngame)
            button11.grid(row=13, column=0)

def bonus(i):
    if i <55:
        if one[0] != -1 and two[0] != -1 and three[0] != -1 and four[0] != -1 and five[0] != -1 and six[0] != -1:
                topscore = one[0]+two[0]+three[0]+four[0]+five[0]+six[0]
                if topscore >= 63:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 9, column = i, sticky = NSEW)
                    point = Label(root, text = str(35), relief = SOLID)
                    point.grid(row = 9, column = i, sticky = NSEW)
                    text7.set(str(" "))
                    topscore += 35
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 10, column = i, sticky = NSEW)
                    point = Label(root, text = str(topscore), relief = SOLID)
                    point.grid(row = 10, column = i, sticky = NSEW)
                else:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 9, column = i, sticky = NSEW)
                    point = Label(root, text = str(0), relief = SOLID)
                    point.grid(row = 9, column = i, sticky = NSEW)
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 10, column = i, sticky = NSEW)
                    point = Label(root, text = str(topscore), relief = SOLID)
                    point.grid(row = 10, column = i, sticky = NSEW)
                tot(topscore,i)
    if i > 56:
        print(one1,two1,three1,four1,five1,six1)
        if one1 != [-1] and two1 != [-1] and three1 != [-1] and four1 != [-1] and five1 != [-1] and six1 != [-1]:
                topscore = one1[0]+two1[0]+three1[0]+four1[0]+five1[0]+six1[0]
                if topscore >= 63:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 9, column = i, sticky = NSEW)
                    point = Label(root, text = str(35), relief = SOLID)
                    point.grid(row = 9, column = i, sticky = NSEW)
                    text7.set(str(" "))
                    topscore += 35
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 10, column = i, sticky = NSEW)
                    point = Label(root, text = str(topscore), relief = SOLID)
                    point.grid(row = 10, column = i, sticky = NSEW)
                else:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 9, column = i, sticky = NSEW)
                    point = Label(root, text = str(0), relief = SOLID)
                    point.grid(row = 9, column = i, sticky = NSEW)
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 10, column = i, sticky = NSEW)
                    point = Label(root, text = str(topscore), relief = SOLID)
                    point.grid(row = 10, column = i, sticky = NSEW)
                tot(topscore,i)
def bot_tot(score,i, botc,botc2):
    global botscore, botscore2
    if i < 56:
        botscore += score
        if botc == 7:
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 19, column = i, sticky = NSEW)
            point = Label(root, text = str(botscore), relief = SOLID)
            point.grid(row = 19, column = i, sticky = NSEW)
            tot(botscore,i)
    if i > 57:
        botscore2 += score
        if botc2 == 7:
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 19, column = i, sticky = NSEW)
            point = Label(root, text = str(botscore2), relief = SOLID)
            point.grid(row = 19, column = i, sticky = NSEW)
            tot(botscore2,i)


def clear(i,j):
    global confirm, rowval, colval, rolled, last_cond,gamecount,last_num, botcount, botcount2
    if rowval == i and colval ==j+2+gamecount:
        endturn()
        last_num[0] = -1
        last_cond[0] = False
        rolled = True
        confirm = False
        text7.set(str(" "))
        point = Label(root, textvariable = text7, relief = SOLID)
        point.grid(row = i, column = j+2, sticky = NSEW)
        if rowval > 11 and colval < 56:
            botcount -= 1
            print(botcount)
        if rowval > 11 and colval > 56:
            botcount2 -= 1
            print(botcount2)

def make_table():
    global gamecount, i
    for i in [0,7]:
        L1 = tk.Label(root, text ="Upper Section", relief=SOLID)
        L1.grid(row = 2, column = 50+i,sticky = NSEW)
        L2 = tk.Label(root, text ="Game 1", relief=SOLID, bg = "green")
        L2.grid(row = 2, column = 51+i,sticky = NSEW)
        L3 = tk.Label(root, text ="Game 2", relief=SOLID)
        L3.grid(row = 2, column = 52+i,sticky = NSEW)
        L4 = tk.Label(root, text ="Game 3", relief=SOLID)
        L4.grid(row = 2, column = 53+i,sticky = NSEW)
        L5 = tk.Label(root, text ="Game 4", relief=SOLID)
        L5.grid(row = 2, column = 54+i,sticky = NSEW)
        L6 = tk.Label(root, text ="Game 5", relief=SOLID)
        L6.grid(row = 2, column = 55+i,sticky = NSEW)
        L7 = tk.Button(root, text = "Aces = 1", relief=SOLID, command =lambda k = 3,j=50+i: aces(k,j))
        L7.grid(row = 3, column = 50+i,sticky = NSEW)
        L8 = tk.Button(root, text = "Twos = 2", relief=SOLID, command =lambda k = 4,j=50+i: twos(k,j))
        L8.grid(row = 4, column = 50+i,sticky = NSEW)
        L9 = tk.Button(root, text = "Threes = 3", relief=SOLID, command = lambda k = 5,j=50+i:threes(k,j))
        L9.grid(row = 5, column = 50+i,sticky = NSEW)
        L10 = tk.Button(root, text = "Fours = 4", relief=SOLID, command = lambda k = 6,j=50+i: fours(k,j))
        L10.grid(row = 6, column = 50+i,sticky = NSEW)
        L11 = tk.Button(root, text = "Fives = 5", relief=SOLID, command = lambda k = 7,j=50+i:fives(k,j))
        L11.grid(row = 7, column = 50+i,sticky = NSEW)
        L12 = tk.Button(root, text = "Sixes = 6", relief=SOLID, command = lambda k = 8,j=50+i:sixes(k,j))
        L12.grid(row = 8, column = 50+i,sticky = NSEW)
        L20 = tk.Label(root, text = "Upper Bonus", relief=SOLID)
        L20.grid(row = 9, column = 50+i,sticky = NSEW)
        L20 = tk.Label(root, text = "Upper Total", relief=SOLID)
        L20.grid(row = 10, column = 50+i,sticky = NSEW)
        L13 = tk.Label(root, text ="Lower Section", relief=SOLID)
        L13.grid(row = 11, column = 50+i,sticky = NSEW)
        L14 = tk.Button(root, text = "3 of a Kind", relief=SOLID, command = lambda k = 12,j=50+i:tkind(k,j))
        L14.grid(row = 12, column = 50+i,sticky = NSEW)
        L15 = tk.Button(root, text = "4 of a Kind", relief=SOLID, command = lambda k = 13,j=50+i:fkind(k,j))
        L15.grid(row = 13, column = 50+i,sticky = NSEW)
        L16 = tk.Button(root, text = "Full House", relief=SOLID, command =lambda k = 14,j=50+i: fhouse(k,j))
        L16.grid(row = 14, column = 50+i,sticky = NSEW)
        L17 = tk.Button(root, text = "Sm. Straight", relief=SOLID, command =lambda k = 15,j=50+i: sstraight(k,j))
        L17.grid(row = 15, column = 50+i,sticky = NSEW)
        L18 = tk.Button(root, text = "Lg. Straight", relief=SOLID, command = lambda k = 16,j=50+i:lstraight(k,j))
        L18.grid(row = 16, column = 50+i,sticky = NSEW)
        L19 = tk.Button(root, text = "Chance", relief=SOLID, command = lambda k = 17,j=50+i:chance(k,j))
        L19.grid(row = 17, column = 50+i,sticky = NSEW)
        L20 = tk.Button(root, text = "Yahtzee", relief=SOLID, command = lambda k = 18,j=50+i: yahtzee(k,j))
        L20.grid(row = 18, column = 50+i,sticky = NSEW)
        L20 = tk.Label(root, text = "Lower Total", relief=SOLID)
        L20.grid(row = 19, column = 50+i,sticky = NSEW)
        L20 = tk.Label(root, text = "Total", relief=SOLID)
        L20.grid(row = 20, column = 50+i,sticky = NSEW)
        for rows in range(18):
            button9 = tk.Button(root, text="Clear", command = lambda k = rows+3, j = 49+i: clear(k,j))
            button9.grid(row=rows+3, column=49+i)
            for cols in range(5):
                if rows == 8:
                    larb = Label(root, bg = "black", relief = SOLID)
                    larb.grid(row = rows+3, column = cols+(51+i), sticky = NSEW)
                else:
                    larb = Label(root, textvariable = " " ,relief = SOLID)
                    larb.grid(row = rows+3, column = cols+(51+i), sticky = NSEW)
    
def aces(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5, one, two, three, four, five, six, topcount, rowval, colval, one1,two1,three1,four1,five1,six1, one_cond,rolled, games, gamecount,last_cond, one_cond1, last_num
    if rolled == True:
        rowval,colval = k,j+gamecount+1
        sum = 0
        nums = [dice_index, dice_index2, dice_index3, dice_index4, dice_index5]
        if confirm == False:
            if turn == True:
                if one_cond[0] == False:
                    one_cond = [True]
                    last_cond = one_cond
                    i = games[gamecount]
                    for x in nums:
                        if x == 1:
                            sum += 1
                    one = [sum]
                    last_num = one
                    bonus(i)
            else:
                if one_cond1[0] == False:
                    one_cond1 = [True]
                    last_cond = one_cond1
                    i = games[gamecount+5]
                    for x in nums:
                        if x == 1:
                            sum += 1
                    one1 = [sum]
                    last_num = one1
                    bonus(i)
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 3, column = i, sticky = NSEW)
            point = Label(root, text = str(sum), relief = SOLID)
            point.grid(row = 3, column = i, sticky = NSEW)
            confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)       
def twos(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5, one, two, three, four, five, six, topcount, rowval, colval, one1,two1,three1,four1,five1,six1,two_cond,two_cond1,rolled, games, gamecount, last_num, last_cond
    if rolled == True:    
            rowval,colval = k,j+gamecount+1
            sum = 0
            nums = [dice_index, dice_index2, dice_index3, dice_index4, dice_index5]
            if confirm == False:
                if turn == True:
                    if two_cond[0] == False:
                        two_cond = [True]
                        last_cond = two_cond
                        i = games[gamecount]
                        for x in nums:
                            if x == 2:
                                sum += 2
                        two = [sum]
                        last_num = two
                        bonus(i)
                else:
                    if two_cond1[0] == False:
                        two_cond1 = [True]
                        last_cond = two_cond1
                        i = games[gamecount+5]
                        for x in nums:
                            if x == 2:
                                sum += 2
                        two1 = [sum]
                        last_num = two1
                        bonus(i)
                text8.set(str(" "))
                point = Label(root, textvariable = text8, relief = SOLID)
                point.grid(row = 4, column = i, sticky = NSEW)
                point = Label(root, text = str(sum), relief = SOLID)
                point.grid(row = 4, column = i, sticky = NSEW)
                confirm = True
                endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)       
def threes(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5, one, two, three, four, five, six, topcount, rowval, colval, one1,two1,three1,four1,five1,six1,three_cond, rolled, games, gamecount, last_num, last_cond, three_cond1
    if rolled == True:
        rowval,colval = k,j+gamecount+1
        sum = 0
        nums = [dice_index, dice_index2, dice_index3, dice_index4, dice_index5]
        if confirm == False:
            if turn == True:
                if three_cond[0] == False:
                    three_cond = [True]
                    last_cond = three_cond
                    i = games[gamecount]
                    for x in nums:
                        if x == 3:
                            sum += 3
                    three = [sum]
                    last_num = three
                    bonus(i)
            else:
                if three_cond1[0] == False:
                    three_cond1 = [True]
                    last_cond = three_cond1
                    i = games[gamecount+5]
                    for x in nums:
                        if x == 3:
                            sum += 3
                    three1 = [sum]
                    last_num = three1
                    bonus(i)
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 5, column = i, sticky = NSEW)
            point = Label(root, text = str(sum), relief = SOLID)
            point.grid(row = 5, column = i, sticky = NSEW)
            confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)        
def fours(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5, one, two, three, four, five, six, topcount, rowval, colval, one1,two1,three1,four1,five1,six1,four_cond,rolled, games, gamecount, last_num, four_cond1,last_cond
    if rolled == True:    
        rowval,colval = k,j+gamecount+1
        sum = 0
        nums = [dice_index, dice_index2, dice_index3, dice_index4, dice_index5]
        if confirm == False:
            if turn == True:
                if four_cond[0] == False:
                    four_cond = [True]
                    last_cond = four_cond
                    i = games[gamecount]
                    for x in nums:
                        if x == 4:
                            sum += 4
                    four = [sum]
                    last_num = four
                    bonus(i)
            else:
                if four_cond1[0] == False:
                    four_cond1 = [True]
                    last_cond = four_cond1
                    i = games[gamecount+5]
                    for x in nums:
                        if x == 4:
                            sum += 4
                    four1 = [sum]
                    last_num = four1
                    bonus(i)
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 6, column = i, sticky = NSEW)
            point = Label(root, text = str(sum), relief = SOLID)
            point.grid(row = 6, column = i, sticky = NSEW)
            confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)        
def fives(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5, one, two, three, four, five, six, topcount, rowval, colval, one1,two1,three1,four1,five1,six1, five_cond,rolled, games, gamecount, last_num, last_cond,five_cond1
    if rolled == True:   
        rowval,colval = k,j+gamecount+1
        sum = 0
        nums = [dice_index, dice_index2, dice_index3, dice_index4, dice_index5]
        if confirm == False:
            if turn == True:
                if five_cond[0] == False:
                    five_cond = [True]
                    last_cond = five_cond
                    i = games[gamecount]
                    for x in nums:
                        if x == 5:
                            sum += 5
                    five = [sum]
                    last_num = five
                    bonus(i)
            else:
                if five_cond1[0] == False:
                    five_cond1 = [True]
                    last_cond = five_cond1
                    i = games[gamecount+5]
                    for x in nums:
                        if x == 5:
                            sum += 5
                    five1 = [sum]
                    last_num = five1
                    bonus(i)
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 7, column = i, sticky = NSEW)
            point = Label(root, text = str(sum), relief = SOLID)
            point.grid(row = 7, column = i, sticky = NSEW)
            confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)        
def sixes(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5, one, two, three, four, five, six, topcount, rowval, colval, one1,two1,three1,four1,five1,six1,six_cond,rolled, games, gamecount, last_num, last_cond, six_cond1
    if rolled == True: 
        rowval,colval = k,j+gamecount+1
        sum = 0
        nums = [dice_index, dice_index2, dice_index3, dice_index4, dice_index5]
        if confirm == False:
            if turn == True:
                if six_cond[0] == False:
                    six_cond = [True]
                    last_cond = six_cond
                    i = games[gamecount]
                    for x in nums:
                        if x == 6:
                            sum += 6
                    six = [sum]
                    last_num = six
                    bonus(i)
            else:
                if six_cond1[0] == False:
                    six_cond1 = [True]
                    last_cond = six_cond1
                    i = games[gamecount+5]
                    for x in nums:
                        if x == 6:
                            sum += 6
                    six1 = [sum]
                    last_num = six1
                    bonus(i)
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 8, column = i, sticky = NSEW)
            point = Label(root, text = str(sum), relief = SOLID)
            point.grid(row = 8, column = i, sticky = NSEW)
            confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)       
def tkind(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5,rowval, colval,rolled, botcount, botcount2, games, gamecount, tkind_cond, last_cond, tkind_cond1
    if rolled == True:
            rowval,colval = k,j+gamecount+1
            nums = [dice_index,dice_index2,dice_index3,dice_index4,dice_index5]
            if confirm == False:
                if turn == True:
                    if tkind_cond[0] == False:
                        tkind_cond = [True]
                        last_cond = tkind_cond
                        botcount+=1
                        i = games[gamecount]
                else:
                    if tkind_cond1[0] == False:
                        tkind_cond1 = [True]
                        last_cond = tkind_cond1
                        botcount2+=1
                        i = games[gamecount+5]
                a = Counter(nums)
                a = a.most_common()
                if a[0][1] >= 3:
                    score = sum(nums)
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 12, column = i, sticky = NSEW)
                    point = Label(root, text = str(score), relief = SOLID)
                    point.grid(row = 12, column = i, sticky = NSEW)
                    bot_tot(score, i, botcount, botcount2)
                    confirm = True
                else:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 12, column = i, sticky = NSEW)
                    point = Label(root, text = str(0), relief = SOLID)
                    point.grid(row = 12, column = i, sticky = NSEW)
                    confirm = True
                    bot_tot(0, i, botcount, botcount2)
                endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)

def fkind(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5,rowval, colval,rolled, botcount, botcount2, games, gamecount, fkind_cond, last_cond, fkind_cond1, check
    if rolled == True:
        rowval,colval = k,j+gamecount+1
        nums = [dice_index,dice_index2,dice_index3,dice_index4,dice_index5]
        if confirm == False:
            if turn == True:
                if fkind_cond[0] == False:
                    fkind_cond = [True]
                    last_cond = fkind_cond
                    botcount+=1
                    i = games[gamecount]
            else:
                if fkind_cond1[0] == False:
                    fkind_cond1 = [True]
                    last_cond = fkind_cond1
                    botcount2+=1
                    i = games[gamecount+5]
            a = Counter(nums)
            a = a.most_common()
            if a[0][1] >= 4:
                if check == True:
                    L15 = tk.Button(root, text = "4 of a Kind", relief=SOLID, bg = 'yellow', command = lambda k = 13,j=50+i:fkind(k,j))
                    L15.grid(row = 13, column = 50+i,sticky = NSEW)
                else:
                    score = sum(nums)
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 13, column = i, sticky = NSEW)
                    point = Label(root, text = str(score), relief = SOLID)
                    point.grid(row = 13, column = i, sticky = NSEW)
                    bot_tot(score, i, botcount, botcount2)
                    confirm = True
            else:
                text7.set(str(" "))
                point = Label(root, textvariable = text7, relief = SOLID)
                point.grid(row = 13, column = i, sticky = NSEW)
                point = Label(root, text = str(0), relief = SOLID)
                point.grid(row = 13, column = i, sticky = NSEW)
                bot_tot(0, i, botcount, botcount2)
                confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)
def fhouse(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5,rowval, colval,rolled, botcount, botcount2, games, gamecount, fhouse_cond, last_cond, fhouse_cond1
    if rolled == True:
        rowval,colval = k,j+gamecount+1
        nums = [dice_index,dice_index2,dice_index3,dice_index4,dice_index5]
        if confirm == False:
            if turn == True:
                if fhouse_cond[0] == False:
                    fhouse_cond = [True]
                    last_cond = fhouse_cond
                    botcount+=1
                    i = games[gamecount]
            else:
                if fhouse_cond1[0] == False:
                    fhouse_cond1 = [True]
                    last_cond = fhouse_cond1
                    botcount2+=1
                    i = games[gamecount+5]
            a = Counter(nums)
            a = a.most_common()
            if len(a) == 2:
                if a[0][1] == 3 and a[1][1] == 2:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 14, column = i, sticky = NSEW)
                    point = Label(root, text = str(25), relief = SOLID)
                    point.grid(row = 14, column = i, sticky = NSEW)
                    bot_tot(25, i, botcount, botcount2)
                    confirm = True
                else:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 14, column = i, sticky = NSEW)
                    point = Label(root, text = str(0), relief = SOLID)
                    point.grid(row = 14, column = i, sticky = NSEW)
                    bot_tot(0, i, botcount, botcount2)
                    confirm = True
            else:
                text7.set(str(" "))
                point = Label(root, textvariable = text7, relief = SOLID)
                point.grid(row = 14, column = i, sticky = NSEW)
                point = Label(root, text = str(0), relief = SOLID)
                point.grid(row = 14, column = i, sticky = NSEW)
                bot_tot(0, i, botcount, botcount2)
                confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)
def sstraight(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5,rowval, colval,rolled, botcount, botcount2, games, gamecount, sstraight_cond, last_cond,sstraight_cond1
    if rolled == True:
        rowval,colval = k,j+gamecount+1
        nums = [dice_index,dice_index2,dice_index3,dice_index4,dice_index5]
        if confirm == False:
            if turn == True:
                if sstraight_cond[0] == False:
                    sstraight_cond = [True]
                    last_cond = sstraight_cond
                    botcount+=1
                    i = games[gamecount]
            else:
                if sstraight_cond1[0] == False:
                    sstraight_cond1 = [True]
                    last_cond = sstraight_cond1
                    botcount2+=1
                    i = games[gamecount+5]
            nums.sort()
            last = 0
            for x in nums:
                if x == last:
                    nums.remove(x)
                last = x
            s = len(nums) -1
            if s >= 3:
                if nums[1] - nums[0] == 1 and nums[2]-nums[1] == 1 and nums[3]-nums[2]==1 or nums[s] - nums[s-1] == 1 and nums[s-1]-nums[s-2] == 1 and nums[s-2]-nums[s-3]==1:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 15, column = i, sticky = NSEW)
                    point = Label(root, text = str(30), relief = SOLID)
                    point.grid(row = 15, column = i, sticky = NSEW)
                    bot_tot(30, i, botcount, botcount2)
                    confirm = True
                else:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 15, column = i, sticky = NSEW)
                    point = Label(root, text = str(0), relief = SOLID)
                    point.grid(row = 15, column = i, sticky = NSEW)
                    bot_tot(0, i, botcount, botcount2)
                    confirm = True
            else:
                text7.set(str(" "))
                point = Label(root, textvariable = text7, relief = SOLID)
                point.grid(row = 15, column = i, sticky = NSEW)
                point = Label(root, text = str(0), relief = SOLID)
                point.grid(row = 15, column = i, sticky = NSEW)
                bot_tot(0, i, botcount, botcount2)
                confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)
def lstraight(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5,rowval, colval,rolled, botcount, botcount2, games, gamecount, lstraight_cond, last_cond, lstraight_cond1
    if rolled == True:
        rowval,colval = k,j+gamecount+1
        nums = [dice_index,dice_index2,dice_index3,dice_index4,dice_index5]
        if confirm == False:
            if turn == True:
                if lstraight_cond[0] == False:
                    lstraight_cond = [True]
                    last_cond = lstraight_cond
                    botcount+=1
                    i = games[gamecount]
            else:
                if lstraight_cond1[0] == False:
                    lstraight_cond1 = [True]
                    last_cond = lstraight_cond1
                    botcount2+=1
                    i = games[gamecount+5]
            nums.sort()
            if nums[1] - nums[0] == 1 and nums[2]-nums[1] == 1 and nums[3]-nums[2]==1 and nums[4] - nums[3] == 1:
                text7.set(str(" "))
                point = Label(root, textvariable = text7, relief = SOLID)
                point.grid(row = 16, column = i, sticky = NSEW)
                point = Label(root, text = str(40), relief = SOLID)
                point.grid(row = 16, column = i, sticky = NSEW)
                bot_tot(40, i, botcount, botcount2)
                confirm = True
            else:
                text7.set(str(" "))
                point = Label(root, textvariable = text7, relief = SOLID)
                point.grid(row = 16, column = i, sticky = NSEW)
                point = Label(root, text = str(0), relief = SOLID)
                point.grid(row = 16, column = i, sticky = NSEW)
                bot_tot(0, i, botcount, botcount2)
                confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)
def chance(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5,rowval, colval,rolled, botcount, botcount2, games, gamecount, chance_cond, last_cond, chance_cond1
    if rolled == True:
        rowval,colval = k,j+gamecount+1
        nums = [dice_index,dice_index2,dice_index3,dice_index4,dice_index5]
        if confirm == False:
            if turn == True:
                if chance_cond[0] == False:
                    chance_cond = [True]
                    last_cond = chance_cond
                    botcount+=1
                    i = games[gamecount]
            else:
                if chance_cond1[0] == False:
                    chance_cond1 = [True]
                    last_cond = chance_cond1
                    botcount2+=1
                    i = games[gamecount+5]
            score = sum(nums)
            text7.set(str(" "))
            point = Label(root, textvariable = text7, relief = SOLID)
            point.grid(row = 17, column = i, sticky = NSEW)
            point = Label(root, text = str(score), relief = SOLID)
            point.grid(row = 17, column = i, sticky = NSEW)
            bot_tot(score, i, botcount, botcount2)
            confirm = True
            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)
def yahtzee(k,j):
    global confirm, dice_index, dice_index2, dice_index3, dice_index4, dice_index5, rowval, colval, scoreyat,scoreyat1,rolled, botcount, botcount2, games, gamecount, last_cond
    if rolled == True:
        rowval,colval = k,j+gamecount+1
        nums = [dice_index,dice_index2,dice_index3,dice_index4,dice_index5]
        if confirm == False:
            if turn == True:
                if scoreyat < 0:
                    botcount+=1
                i = games[gamecount]
                a = Counter(nums)
                a = a.most_common()
                if len(a) == 1:
                    scoreyat += 100
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 18, column = i, sticky = NSEW)
                    point = Label(root, text = str(scoreyat), relief = SOLID)
                    point.grid(row = 18, column = i, sticky = NSEW)
                    if scoreyat == 50:
                        bot_tot(scoreyat, i, botcount, botcount2)
                    else:
                        bot_tot(100, i, botcount, botcount2)
                    confirm = True
                else:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 18, column = i, sticky = NSEW)
                    point = Label(root, text = str(0), relief = SOLID)
                    point.grid(row = 18, column = i, sticky = NSEW)
                    bot_tot(0, i, botcount, botcount2)
                    confirm = True
            else:
                if scoreyat1 < 0:
                    botcount2+=1
                i = games[gamecount+5]
                a = Counter(nums)
                a = a.most_common()
                if len(a) == 1:
                    scoreyat1 += 100
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 18, column = i, sticky = NSEW)
                    point = Label(root, text = str(scoreyat1), relief = SOLID)
                    point.grid(row = 18, column = i, sticky = NSEW)
                    if scoreyat1 == 50:
                        bot_tot(scoreyat1, i, botcount, botcount2)
                    else:
                        bot_tot(100, i, botcount, botcount2)
                    confirm = True
                else:
                    text7.set(str(" "))
                    point = Label(root, textvariable = text7, relief = SOLID)
                    point.grid(row = 18, column = i, sticky = NSEW)
                    point = Label(root, text = str(0), relief = SOLID)
                    point.grid(row = 18, column = i, sticky = NSEW)
                    bot_tot(0, i, botcount, botcount2)
                    confirm = True

            endturn()
    else:
        point = Label(root, text = "Bruh... You gotta roll")
        point.grid(row = 18, column = loc3, columnspan = 3)

def click():
    global check
    end = False
    point = Label(root, text = "                                            ")
    point.grid(row = 18, column = loc3, columnspan = 3)
    global continued, continued2, roll_count, dice_index, dice_index2, dice_index3, dice_index4, dice_index5, rolled 
    rolled = True
    if continued != True:
        roll_count = 3
    else:
        if roll_count <= 0:
            text6.set("No more rolls!")
            initialroll= tk.Label(root, textvariable = text6 , fg='black')
            initialroll.grid(row=1, column=loc6, columnspan = 3)
            initialroll = tk.Label(root,text = " ", fg='black')
            initialroll.grid(row=1,column=loc7)
            end = True


    #text1.set(" ")
    #text2.set(" ")
    #text3.set(" ")
    #text4.set(" ")
    #text5.set(" ")
    #show_text(text1,text2,text3,text4,text5)
    """
    Performs the operation of clicking the button. This will roll through
    the different dice heads

    :return: None
    """
    t = 7*5 # start with a time delay of 100 ms and increase it as the dice rolls
    stop = randint(5, 8) # chooses random number between 13 - 17
    for x in range(stop):
        #Dont roll if 3 rolls done
        if end == True:
            break
 # gets the randomly selected dice head by modulo
        
         # gets the randomly selected dice head by modulo
        
         # gets the randomly selected dice head by modulo
        for i in range(0,7):
            if val1 != False:
                dice_list1[i].grid_forget()
            if val2 != False:
                dice_list2[i].grid_forget()
            if val3 !=False:
                dice_list3[i].grid_forget()
            if val4 != False:
                dice_list4[i].grid_forget()
            if val5 != False:
                dice_list5[i].grid_forget()# forgets the grid and restarts
            root.after(t)
        t += 2*5
        if val1 != False:
            dice_index = randint(1,6)
            dice_list1[dice_index].grid(row=1, column=loc1, columnspan=3)
        if val2 != False:
            dice_index2 = randint(1,6)
            dice_list2[dice_index2].grid(row=1, column=loc2, columnspan=3)
        if val3 != False:
            dice_index3 = randint(1,6)
            dice_list3[dice_index3].grid(row=1, column=loc3, columnspan=3)
        if val4 != False:
            dice_index4 = randint(1,6)
            dice_list4[dice_index4].grid(row=1, column=loc4, columnspan=3)
        if val5 != False:
            dice_index5= randint(1,6)
            dice_list5[dice_index5].grid(row=1, column=loc5, columnspan=3)
   
        root.update()
        if x == stop - 1:
            # set text to the selected result
            if val1 != False:
                text1.set(str(dice_index))
            if val2 != False:
                text2.set(str(dice_index2))
            if val3 != False:
                text3.set(str(dice_index3))
            if val4 != False:
                text4.set(str(dice_index4))
            if val5 != False:
                text5.set(str(dice_index5))
            roll_count -= 1
            continued = True
            initialroll = tk.Label(root, text = str(roll_count), fg='black')
            initialroll.grid(row=1, column=loc7, columnspan=3)
            show_text(text1,text2,text3,text4,text5)
            check = True
            #fkind()
            break

def hold1():
    global val1
    if val1 == True:
        val1 = False
        result1 = tk.Label(root, text="holding", fg='red')
        result1.grid(row=4, column=loc1, columnspan=3)
    else:
        result1 = tk.Label(root, text="             ", fg='red')
        result1.grid(row=4, column=loc1, columnspan=3)
        val1 = True
def hold2():
    global val2
    if val2 == True:
        val2 = False
        result1 = tk.Label(root, text="holding", fg='red')
        result1.grid(row=4, column=loc2, columnspan=3)
    else:
        result1 = tk.Label(root, text="             ", fg='red')
        result1.grid(row=4, column=loc2, columnspan=3)
        val2 = True
def hold3():
    global val3
    if val3 == True:
        val3 = False
        result1 = tk.Label(root, text="holding", fg='red')
        result1.grid(row=4, column=loc3, columnspan=3)
    else:
        result1 = tk.Label(root, text="             ", fg='red')
        result1.grid(row=4, column=loc3, columnspan=3)
        val3 = True
def hold4():
    global val4
    if val4 == True:
        val4 = False
        result1 = tk.Label(root, text="holding", fg='red')
        result1.grid(row=4, column=loc4, columnspan=3)
    else:
        result1 = tk.Label(root, text="             ", fg='red')
        result1.grid(row=4, column=loc4, columnspan=3)
        val4 = True
def hold5():
    global val5
    if val5 == True:
        val5 = False
        result1 = tk.Label(root, text="holding", fg='red')
        result1.grid(row=4, column=loc5, columnspan=3)
    else:
        result1 = tk.Label(root, text="             ", fg='red')
        result1.grid(row=4, column=loc5, columnspan=3)
        val5 = True
def endturn():
    global continued, confirm, val1,val2,val3,val4,val5, turn, rolled, check
    check = False
    rolled = False
    if turn == True:
        P1 = tk.Label(root, text="Player 1", fg='black',bg = 'white')
        P1.grid(row=1,column = 52)
        P2 = tk.Label(root, text="Player 2", fg='black', bg = 'yellow')
        P2.grid(row=1,column = 59)
        turn = False
    else:
        P1 = tk.Label(root, text="Player 1", fg='black',bg = 'yellow')
        P1.grid(row=1,column = 52)
        P2 = tk.Label(root, text="Player 2", fg='black', bg = 'white')
        P2.grid(row=1,column = 59)
        turn = True
    val1, val2, val3, val4, val5 = False, False, False, False, False
    hold1()
    hold2()
    hold3()
    hold4()
    hold5()
    continued = False
    text6.set(" ")
    initialroll= tk.Label(root, textvariable = text6, fg='black')
    initialroll.grid(row=1, column=loc6)
    initialroll= tk.Label(root, text = "Rolls remaining:", fg='black')
    initialroll.grid(row=1, column=loc6)
    initialroll = tk.Label(root,text = "3", fg='black')
    initialroll.grid(row=1,column=loc7)
    confirm = False
# create the window form
root = tk.Tk()
root.title("Yahtzee v1.0!")

    # StringVar() updates result label automatically
text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()
text4 = tk.StringVar()
text5 = tk.StringVar()
text6 = tk.StringVar()
text7 = tk.StringVar()
text8 = tk.StringVar()
    # set initial value of text
text1.set("")
text2.set("")
text3.set("")
text4.set("")
text5.set("")
text6.set("")

def show_text(text1,text2,text3,text4,text5):

    # create the result label
    result1 = tk.Label(root, textvariable=text1, fg='black')
    result1.grid(row=3, column=loc1, columnspan=3)
    result2 = tk.Label(root, textvariable=text2, fg='black')
    result2.grid(row=3, column=loc2, columnspan=3)
    result3 = tk.Label(root, textvariable=text3, fg='black')
    result3.grid(row=3, column=loc3, columnspan=3)
    result4 = tk.Label(root, textvariable=text4, fg='black')
    result4.grid(row=3, column=loc4, columnspan=3)
    result5 = tk.Label(root, textvariable=text5, fg='black')
    result5.grid(row=3, column=loc5, columnspan=3)


dice_list1 = create_dice()
dice_list2 = create_dice()
dice_list3 = create_dice()
dice_list4 = create_dice()
dice_list5 = create_dice()

# Display 3 rolls remaining (Intial)
initialroll= tk.Label(root, text = "Rolls remaining:", fg='black')
initialroll.grid(row=1, column=loc6)
initialroll = tk.Label(root,text = "3", fg='black')
initialroll.grid(row=1,column=loc7)

P1 = tk.Label(root, text="Player 1", fg='black',bg = 'yellow')
P1.grid(row=1,column = 52)
#P1 = tk.Entry(root, relief = SOLID)
#P1.grid(row=1,column = 50,sticky = NSEW)

P2 = tk.Label(root, text="Player 2", fg='black')
P2.grid(row=1,column = 59)
#P2 = tk.Entry(root, relief = SOLID)
#P2.grid(row=1,column = 57,sticky = NSEW)
# start with an empty canvas
dice_list1[0].grid(row=1, column=loc1, columnspan=3)
dice_list2[0].grid(row=1, column=loc2, columnspan=3)
dice_list3[0].grid(row=1, column=loc3, columnspan=3)
dice_list4[0].grid(row=1, column=loc4, columnspan=3)
dice_list5[0].grid(row=1, column=loc5, columnspan=3)
table= make_table()

button1 = tk.Button(root, text="Roll", command=click)
button1.grid(row=10, column=0, padx=3)
button2 = tk.Button(root, text="Quit", command=root.destroy)
button2.grid(row=11, column=0, padx=3)
button3 = tk.Button(root, text="Keep/Release", command = hold1)
button3.grid(row=5, column=loc1+1)
button4 = tk.Button(root, text="Keep/Release", command = hold2)
button4.grid(row=5, column=loc2+1)
button5 = tk.Button(root, text="Keep/Release", command = hold3)
button5.grid(row=5, column=loc3+1)
button6 = tk.Button(root, text="Keep/Release", command = hold4)
button6.grid(row=5, column=loc4+1)
button7 = tk.Button(root, text="Keep/Release", command = hold5)
button7.grid(row=5, column=loc5+1)
#button9 = tk.Button(root, text="End Turn", command = endturn)
#button9.grid(row=12, column=0, padx=3)
button11 = tk.Button(root, text="Next Game", command = ngame, state = "disabled")
button11.grid(row=13, column=0,padx=3)

# start of program event loop
root.mainloop()
