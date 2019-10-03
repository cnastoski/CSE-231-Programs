#==============================================================================
#       Project 10
#           Algorithm
#display opening banner
#prompt user to enter a space separated string with the move along with the two 
#cards he wants to move
#for each move call the corresponding function to error check and execute the move
#after each move call a function to check if the user has won, break if won
#If a move is invalid, raise an error to handle it and reprompt for another
#pull up a menu when the user prompts for it
#restart the game if the the user prompts for it
#if the user quits or wins, end the program
#==============================================================================

import cards #This is necessary for the project


BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """

    Game commands:
    
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
    
"""
   
     
def valid_fnd_move(src_card, dest_card):
    """
    inputs are the two cards the user wants to move, raises an error if the 
    move is invalid, returns nothing and continues the code if the moves are 
    valid. Validates a move to the foundation.
    """
    if src_card.rank() == 1 and dest_card == None:
        return #moves the card to fnd if it is an ace
    if src_card.rank() != 1 and dest_card == None: 
        raise RuntimeError("Invalid move: A foundation must start with an ace")
        #raise an error if the first card to the foundation is not an ace
    if dest_card.suit() != src_card.suit():
        raise RuntimeError("Invalid move: Wrong Suit")
        #all the cards on one foundation must be the same suit
    if dest_card.rank() +1 != src_card.rank():
        raise RuntimeError("invalid move: Wrong Rank")
        #the next card placed on a fnd must be one larger than the last
    return    #return to the code    

     
def valid_tab_move(src_card, dest_card):
    """
    inputs are the two cards the user wants to move, raises an error if the 
    move is invalid, returns nothing and continues the code if the moves are 
    valid. Validates a move to the tableau.
    """ 
    if src_card.rank() != dest_card.rank() - 1:
        raise RuntimeError("Invalid Move: card must be one lower")
        #the next card on a tableau must be one lower than the previous one
    if src_card.suit() != dest_card.suit():
        raise RuntimeError("Invalid Move: Wrong Suit")
        #any card moved must be the same suit as the last
    return #return to the code
    
    
def tableau_to_cell(tab, cell):
    """
    inputs are two lists. checks to see if either is empty and moves the card from 
    tab to cell and returns nothing.
    """
    
    if len(tab) == 0: #cannot move a card if there isn't one
        raise RuntimeError("Invalid Move: tableaus cannot be empty")
    if len(cell) == 0: #any card can be placed on an empty cell
        cell.append(tab.pop()) #moves the card from the tab to the cell
    else:  #raises an error if there is a card in the cell
      raise RuntimeError("Invalid move: only one card can be in a cell at a \
time")
    
    pass
            
            
def tableau_to_foundation(tab, fnd):
    """
    inputs are two lists. Error checks to see if the move is valid, then moves the card from 
    tab to fnd and returns nothing. discards the last card if another is placed on
    the foundation
    """   
    if len(tab) == 0: #cannot move a card from an empty list
        raise RuntimeError("Invalid Move: No card to move")
    if len(fnd) == 0: #if the fnd is empty, set the dest card as none and call validation function
        src_card = tab[-1] #the last card in the list
        dest_card = None #no card, since the fnd is empty
        valid_fnd_move(src_card, dest_card)#check to see if the move is valid
        fnd.append(tab.pop())#remove the card from tab and move it to fnd
    else:# if the fuondation already has a card in it
        src_card = tab[-1] #the last cards in fnd and tab
        dest_card = fnd[-1]
        valid_fnd_move(src_card, dest_card) #validate move
        fnd.pop()#discard the last card from fnd
        fnd.append(tab.pop())#move the card from tab to fnd
    pass  
            
            
def tableau_to_tableau(tab1, tab2):
    """
    inputs are two lists. Error checks to see if the move is valid, then moves the card from 
    tab1 to tab2 and returns nothing.
    """  
    if len(tab1) == 0: #no card
        raise RuntimeError("Invalid move: No card to move")
    if (tab2) == 0:#can put any card on an empty tab
        tab2.append(tab1.pop())#move card from tab1 to tab2
    else:
        src_card = tab1[-1]
        dest_card = tab2[-1]
        valid_tab_move(src_card, dest_card)
        tab2.append(tab1.pop())
    pass

def cell_to_foundation(cell, fnd):
    """
    inputs are two lists. Error checks to see if the move is valid, then moves the card from 
    cell to foundation and returns nothing. Discards the last card from fnd 
    if another is placed on top of it
    """  
    if len(cell) == 0:
        raise RuntimeError("Invalid move: No card to move")
    if len(fnd) == 0:#set dest card as none and call funcions to validate and move the card
        dest_card = None
        src_card = cell[-1]
        valid_fnd_move(src_card, dest_card)
        fnd.append(cell.pop())
    else:
        src_card = cell[-1]
        dest_card = fnd[-1]
        valid_fnd_move(src_card, dest_card)
        fnd.pop()#discards the last card
        fnd.append(cell.pop())
    pass 


def cell_to_tableau(cell, tab):
    """
    inputs are two lists. Error checks to see if the move is valid, then moves the card from 
    one list to the other and returns nothing.
    """
    if len(cell) == 0:
        raise RuntimeError("Invalid move: cell cannot be empty")
    if len(tab) == 0:
        dest_card = None
        src_card = cell[-1]
        valid_fnd_move(src_card, dest_card)
        tab.append(cell.pop())
    else:
        src_card = cell[-1]
        dest_card = tab[-1]
        valid_tab_move(src_card, dest_card)
        tab.append(cell.pop())
    pass  #Replace this pass statement with your own code
              
              
def is_winner(foundations):
    """
    takes in a list of lists. if all of the lists have a king in each of them,
    declares a win and ends the game. Returns True if the game is won,
    returns False if not.
    """    
    winner = False #set win condition as false
    win_lst = [] #initilize list
    for i in range(0,4): #iterate through each item in the foundations list
        if foundations[i] == []: #if the foundation is empty, the game is not won
            winner = False
            return winner
            break
        if foundations[i][0].rank() != 13:
            winner = False
            return winner
            break
        if foundations[i][0].rank() == 13: #if if is a king, add a True bool to a list
            winner = True  
            win_lst.append(winner) 
        if win_lst == [True,True,True,True]: #only if all four foundations are kings, return True
            winner = True
            return winner


def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """
    
    stock = cards.Deck() #initilize the deck
#    stock.shuffle() #shuffles the deck
    cells = [[], [], [], []]                    #list of 4 lists
    foundations = [[], [], [], []]              #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []] #list of 8 lists
 
        
    
    """ YOUR SETUP CODE GOES HERE """
    
    while len(stock) != 0: #loops while the deck is not empty
        for item in tableaus:
            item.append(stock.deal())
            #adds a card to each tableau from left to right until there are no cards left
            if len(stock) == 0: #stops when the deck is empty
                break
    
    return cells, foundations, tableaus #returns 3 lists of lists


def display_game(cells, foundations, tableaus):
    """
    takes in three lists of lists as inputs. formats the game table nicely and 
    prints out the layout of the game. Returns nothing.
    """
    fnds = foundations
    #Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    print("    ", end="")
    for c in range(len(cells)):
        try:
            print("[{:s}]".format(str(cells[c][-1])), end = " ")
        except IndexError:
            print("[  ]", end = " ")
            
    for c in range(len(fnds)):
        try:
            print(" [{:s}]".format(str(fnds[c][-1])),end = " ")
        except IndexError:
            print(" [  ]", end = " ")
    # to print a card using formatting, convert it to string:
    # print("{}".format(str(card)))

    print()
    #Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    
    tab_lst=max([len(x)for x in tableaus]) #finds the maximum tab
    for i in range(tab_lst): #iterates from 0 to the max amount
        row=[]
        for item in tableaus:
            if len(item)>i: #if the list has less items than the max fill that with whitespace
                row.append(item[i])#else add that item
            else:
                row.append("")
        print("{:>9}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}".format(str(row[0]),\
str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5])\
,str(row[6]),str(row[7])))

        
    
        
def main():
    
    print(RULES) #rules banner
    cells, fnds, tabs = setup_game() #initilize the game
    display_game(cells, fnds, tabs) #print out the game nicely
    print(MENU) #a list of all of the available moves
    command = input("prompt :> ").strip().lower() #the user's input
    while command != 'q': #keeps looping until the user quits
        cmd_lst = command.split(" ") # turns the input into a list of three values
        try:
            if cmd_lst[0] == "tc": #moves from tableau to cell
                tab = tabs[int(cmd_lst[1]) -1] #the user's chosen tableau
                cell = cells[int(cmd_lst[2]) -1]#user's chosen cell
                tableau_to_cell(tab, cell)#validates and moves the card
            if cmd_lst[0] == "tf":#moves from tableau to foundation
                tab = tabs[int(cmd_lst[1]) -1]
                fnd = fnds[int(cmd_lst[2]) -1]#the user's chosen foundation
                tableau_to_foundation(tab, fnd)
            if cmd_lst[0] == "tt":#moves from tableau to tableau
                tab1 = tabs[int(cmd_lst[1]) -1]#tableau 1
                tab2 = tabs[int(cmd_lst[2]) -1]#tableau 2
                tableau_to_tableau(tab1, tab2)
            if cmd_lst[0] == "cf":#moves from cell to foundatoin
                cell = cells[int(cmd_lst[1]) -1]
                fnd = fnds[int(cmd_lst[2]) -1]
                cell_to_foundation(cell, fnd)
            if cmd_lst[0] == "ct": #moves from cell to tableau
                cell = cells[int(cmd_lst[1]) -1]
                tab = tabs[int(cmd_lst[2]) -1]
                cell_to_tableau(cell, tab)
            if cmd_lst[0] == "r":#re-shuffles and restarts the game
                cells, fnds, tabs = setup_game()
            if cmd_lst[0] == "h":#calls the move menu
                print(MENU)
        except RuntimeError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
        except IndexError as error_message: #reprompts if the index is out of range
            print("{:s}\nTry again.".format(str(error_message)))
        except ValueError as error_message:#reprompts if the input is not the right type
            print("{:s}\nTry again.".format(str(error_message)))
        win_check = is_winner(fnds)
        
        display_game(cells, fnds, tabs)
        if win_check == True: #checks if the game is won after every turn
            print("Congratulations, you won!") #stops the game if the function returns True.
            break           
        command = input("prompt :> ").strip().lower()

if __name__ == '__main__':
    main()
    
    
# Questions
# Q1: 7
# Q2: 1
# Q3: 1
# Q4: 5
# Q5: 7
