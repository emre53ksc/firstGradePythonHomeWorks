# name : Emre Kesici
# id : 300201041

# this assignment was given on 10.11.2023 and was expected to be done using the most basic python units. 
# no function defining was allowed. you can understand that this is not a real blackjack by looking at the assignment details, some rules vary.

import random 
from random import randint
# the functions we will use to draw random cards
u_point = 1000              #u_point for user point
d_point = 1000              #d_point for dealer point
round = 0                   #round for round number
u_cards = 0                 #sum of users cards
d_cards = 0                 #sum of dealers cards
u_cards_ace = 0             #also sum of users cards but ace accepted 11
d_cards_ace = 0             #also sum of dealers cards but ace accepted 11
# assigned the starting point given to us which is 1000 point
print('Welcome to the game!')

while not (u_point <= 0 or d_point <= 0):           #the game will continue as long as neither side runs out of points
    u_ace = 0                               #if u_ace is 1 there is a ace card in users card and ıt will be accepted 11
    d_ace = 0                               #same for dealer
    end = '*'                               #the variable to end round 
    double_card = ''                        
    want = ''                               
    round += 1
    bet = 0
    d_cards_str = ''                        #cards are stored in str variable and print out
    u_cards_str = ''    
    print('#################################')
    print('round', round)
    print('Current User Point:', u_point,'\nCurrent Dealer Point:', d_point)
    print('################################# \n')
    print ('please place a maximum of', u_point, 'bet')
    while bet > u_point or bet <= 0 or bet > d_point :       #the bet will be accepted for only valid values
        bet = int(input())
    card1 = min(10, randint(1,13))
    card2 = min(10, randint(1,13))
    card3 = min(10, randint(1,13))
    card4 = min(10, randint(1,13))
    d_cards = card1 + card2
    u_cards = card3 + card4
    d_cards_str = str(card1) + ' - ' + str(card2)
    u_cards_str = str(card3) + ' - ' + str(card4)
    if card3 == 1 or card4 == 1 :                   #line 45 to 54 checking ace possiblity and print out for that
        if not u_cards + 10 > 21 :                  #ace can be used 1 or 11 ,and one ace checking is enough
            u_ace = 1                               #if ace can be use with 11 just +10 cards
            u_cards_ace = u_cards + 10          #cannot calculation in str() func so using variable for that            
        else :
            u_ace = 0
    if u_ace == 1 :                             #if ace is true users 1 card will be 11
        print('Dealer has: ? -', card2, '\nUser has:', u_cards_str, '(total:',str(u_cards_ace) + ')')
    elif u_ace == 0 :
        print('Dealer has: ? -', card2, '\nUser has:', u_cards_str, '(total:',str(u_cards) + ')')
    if u_point >= bet*2 :                   #Don't ask about doubling if there are no points to double 
        while not (double_card == 'y' or double_card == 'n') :                                    #ask doubling
            double_card = input('Do you want to draw just one card and double the bet? (y,n)')
        if double_card == 'y' :
            bet *= 2
            new_card = min(10, randint(1,13))
            u_cards += new_card
            u_cards_str = u_cards_str + ' - ' + str(new_card)
            if new_card == 1 :                      #check ace possibilty of new card         
                if not u_cards + 10 > 21 :
                    u_ace = 1
                    u_cards_ace = u_cards + 10
                else :
                    u_ace == 0
            if u_ace == 1 :                         #this option for the probability of a previously ace deck blowing up when drawing a new card 
                if not u_cards + 10 > 21 :
                    u_cards_ace = u_cards + 10
                    print('New Card:', new_card, '\n\nUser has:', u_cards_str, '(total:', str(u_cards_ace) + ')')
                else :
                    u_ace = 0
                    print('New Card:', new_card, '\n\nUser has:', u_cards_str, '(total:', str(u_cards) + ')')
            else :
                print('New Card:', new_card, '\n\nUser has:', u_cards_str, '(total:', str(u_cards) + ')')
            
            if u_ace == 1 :                     #check how you accept ace for the following comparisons 
                u_cards = u_cards_ace

            if u_cards > 21:
                print('Dealer wins the round')
                u_point -= bet
                d_point += bet
                while not end == '':   
                    end = input('Press enter to continue...')
                if end == '' :
                    continue                    #continue is used to start the loop from the beginning again
                
            else :
                if card1 == 1 or card2 == 1 :
                    if not d_cards + 10 > 21 :
                        d_ace = 1
                        d_cards_ace = d_cards + 10                      
                    else :
                        d_ace = 0
                if d_ace == 1 :
                    print('Dealer has:', d_cards_str, '(total:',str(d_cards_ace) + ')')
                elif d_ace == 0 :
                    print('Dealer has:', d_cards_str, '(total:',str(d_cards) + ')')

                if d_ace == 1 :                     #bring the ace to the value we agreed to before entering the card draw check 
                    d_cards = d_cards_ace
                if u_ace == 1 :
                    u_cards = u_cards_ace
                while d_cards < u_cards :               #dealer has to draw cards until his deck exceeds player's totalcards
                    if d_ace == 1 :
                        d_cards = d_cards_ace - 10           #if entered with ace, return to normal for further processing
                    new_card = min(10, randint(1,13)) 
                    d_cards_str = d_cards_str + ' - ' + str(new_card) 
                    d_cards += new_card

                    if new_card == 1 :                  
                        if not d_cards + 10 > 21 :
                            d_ace = 1
                            d_cards_ace = d_cards + 10
                        else :
                            d_ace == 0
                    if d_ace == 1 :
                        if not d_cards + 10 > 21 :
                            d_cards_ace = d_cards + 10
                            print('New Card:', new_card, '\n\nDealer has:', d_cards_str, '(total:', str(d_cards_ace) + ')')
                        else :
                            d_ace = 0
                            print('New Card:', new_card, '\n\nDealer has:', d_cards_str, '(total:', str(d_cards) + ')')
                    else :
                        print('New Card:', new_card, '\n\nDealer has:', d_cards_str, '(total:', str(d_cards) + ')')                    
                    
                    if d_cards > 21:
                        print('user wins the round')
                        u_point += bet
                        d_point -= bet
                        break                           #break was used instead of continue because of the while loop in line 105...
                                                        #... first finish the first while loop and then the round will start again with the continue command.
                if d_ace == 1 :                         #line 134 to 184 last comparison
                    d_cards = d_cards_ace
                
                if d_cards <= 21 :
                    if u_cards > d_cards :
                        print('user wins the round')
                        u_point += bet
                        d_point -= bet
                        while not end == '':   
                            end = input('Press enter to continue...')
                        if end == '' :
                            continue
                    elif d_cards > u_cards :
                        print('Dealer wins the round')
                        u_point -= bet
                        d_point += bet
                        while not end == '':   
                            end = input('Press enter to continue...')
                        if end == '' :
                            continue
                    else :
                        print('draw')
                        while not end == '':   
                            end = input('Press enter to continue...')
                        if end == '' :
                            continue

                else :                  
                    while not end == '':   
                        end = input('Press enter to continue...')
                    if end == '' :
                        continue                    
    if double_card == '' or double_card == 'n' :                    #enter if player reject the doubling question or dont have enough point                                   
        while not (want == 'y' or want == 'n') :
            want = input('Do you want another card? (y,n)')
        if want == 'y' :
            while want == 'y' :                                     #draws new cards as long as the player approves (if its okay)
                new_card = min(10, randint(1,13))
                u_cards += new_card
                u_cards_str = u_cards_str + ' - ' + str(new_card)
                if new_card == 1 :          #check ace possibilty of new card         
                    if not u_cards + 10 > 21 :
                        u_ace = 1
                        u_cards_ace = u_cards + 10
                    else :
                        u_ace == 0
                if u_ace == 1 :
                    if not u_cards + 10 > 21 :
                        u_cards_ace = u_cards + 10
                        print('New Card:', new_card, '\n\nUser has:', u_cards_str, '(total:', str(u_cards_ace) + ')')
                    else :
                        u_ace = 0
                        print('New Card:', new_card, '\n\nUser has:', u_cards_str, '(total:', str(u_cards) + ')')
                else :
                    print('New Card:', new_card, '\n\nUser has:', u_cards_str, '(total:', str(u_cards) + ')')

                if u_cards > 21 :
                    break

                want = input('Do you want another card? (y,n)')

        if u_cards > 21 :
            print('Dealer wins the round')
            u_point -= bet
            d_point += bet
            while not end == '':   
                end = input('Press enter to continue...')
            if end == '' :
                continue
        if want == 'n' :
            if card1 == 1 or card2 == 1 :
                if not d_cards + 10 > 21 :
                    d_ace = 1
                    d_cards_ace = d_cards + 10                     
                else :
                    d_ace = 0
            if d_ace == 1 :
                print('Dealer has:', d_cards_str, '(total:',str(d_cards_ace) + ')')
            elif d_ace == 0 :
                print('Dealer has:', d_cards_str, '(total:',str(d_cards) + ')')
            if d_ace == 1 :
                d_cards = d_cards_ace
            if u_ace == 1 :
                    u_cards = u_cards_ace
            while d_cards < u_cards :               
                if d_ace == 1 :
                    d_cards = d_cards_ace - 10           
                new_card = min(10, randint(1,13)) 
                d_cards_str = d_cards_str + ' - ' + str(new_card) 
                d_cards += new_card
                if new_card == 1 :          #check ace possibilty of new card         
                    if not d_cards + 10 > 21 :
                        d_ace = 1
                        d_cards_ace = d_cards + 10
                    else :
                        d_ace == 0
                if d_ace == 1 :
                    if not d_cards + 10 > 21 :
                        d_cards_ace = d_cards + 10
                        print('New Card:', new_card, '\n\nDealer has:', d_cards_str, '(total:', str(d_cards_ace) + ')')
                    else :
                        d_ace = 0
                        print('New Card:', new_card, '\n\nDealer has:', d_cards_str, '(total:', str(d_cards) + ')')
                else :
                    print('New Card:', new_card, '\n\nDealer has:', d_cards_str, '(total:', str(d_cards) + ')')
                    
                                        
                if d_cards > 21:
                    print('user wins the round')
                    u_point += bet
                    d_point -= bet
                    break
                
            if d_ace == 1 :
                d_cards = d_cards_ace
            if u_ace == 1 :
                u_cards = u_cards_ace
            if d_cards <= 21 :
                if u_cards > d_cards :
                    print('user wins the round')
                    u_point += bet
                    d_point -= bet
                    while not end == '':   
                        end = input('Press enter to continue...')
                    if end == '' :
                        continue
                elif d_cards > u_cards :
                    print('Dealer wins the round')
                    u_point -= bet
                    d_point += bet
                    while not end == '' :   
                        end = input('Press enter to continue...')
                    if end == '' :
                        continue
                else :
                    print('draw')
                    while not end == '':   
                        end = input('Press enter to continue...')
                    if end == '' :
                        continue

            else :                  
                while not end == '':   
                        end = input('Press enter to continue...')
                if end == '' :
                    continue    
if u_point <= 0 :                                       #the end of whole game
    print('GAME OVER \nDealer beats you')
elif d_point <= 0 :
    print('CONGRATULATIONS \nYou beat the game')
