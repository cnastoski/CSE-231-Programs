import cards



def is_winner(foundations):
    """
    takes in a list of lists. if all of the lists have a king in each of them,
    declares a win and ends the game.
    """    
    winner = False #set win condition as false
    win_lst = []#initilize list
    for i in range(0,4): #fiterate through each item in the foundations list
      
            
        if foundations[i] == []:
            winner = False
            return winner
            break
        if foundations[i][0].rank() != 13:
            winner = False
            return winner
            break
        if foundations[i][0].rank() == 13:
            winner = True  
            win_lst.append(winner)
        if win_lst == [True,True,True,True]:
            winner = True
            return winner
         
       
    
a = cards.Card(13,1)
b = cards.Card(13,2)
c = cards.Card(13,3)
d = cards.Card(12,4)
foundation = [[a],[a],[a],[a]]

print(is_winner(foundation))


print("{} {} {} {} {} {} {} {}".format(str(tab[0][y]), str(tab[1][y]),\
 str(tab[2][y]), str(tab[3][y]), str(tab[4][y]), str(tab[5][y]), str(tab[6][y]), str(tab[7][y])))

