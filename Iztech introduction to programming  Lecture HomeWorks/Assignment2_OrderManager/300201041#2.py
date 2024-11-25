def prepareInfo(filename, file, selection):
    option = []                                         #for list of options that the customer will see
    next_code =[]                                       #for list that will identify the next connected options
    f = file.readlines()
    for i in f:
        data = i.strip('\n').split(';')
        if selection :       #if there is a selection for connected opiton, the program needs to enter here to show the connected options
            control = '#' + selection          #only adds data to lists that depends on the option chosen by the customer                     
            if control in data[0] :
                option.append(data[1])
                next_code.append(data[2])
        else :                                  #if there is no connected options
            option.append(data[1])        
    printMenu(option)                           #shows initial options to customer
    while True:                       #for take valid input from user
        user_input = getUserInput(str(filename))    
        if 1 <= user_input <= len(option):      #user cannot chose out of option
            break
        else :
            print('Please enter a valid input.')
    s = option[user_input-1]
    show(s)             #shows the selected option to user
    order.append(s)     #adding last selected option to order list
    if selection :        #27-33 returns the correct data according to which part program is in
        if not next_code[user_input - 1].isalpha() :
            price = float(next_code[user_input - 1])        
            order.append(price)
        else :
            return str(next_code[user_input - 1])
    else :                      
        return str(user_input)                          #returns data to show the selected options in the next section 
    
def printMenu(option):              #prints the options to be shown to the user in sequential order
    n = 0                           
    for item in option:
        n += 1
        print(str(n)+ '. ' + item)

def getUserInput(message):
    while True:                                             #extracts text according to the desired data from the user and receives input  
        q = 'Please select the ' + str(message) + ':'
        user_input = input(q).strip()       #clears blanks in the user's input with stirp func
        user_input = int(user_input)
        if not user_input:
            print("Please enter a input.")
        else:
            return user_input

def show(text):                                             #it shows but in cool way
    print('-' * (50))
    print(text)
    print('-' * (50) + '\n')

show('Welcome to the Store')            #starts
selection_ = ''  
order = []          #for list of all of selected option from user
complete = 'n'              #control variable to continue to take order or not
total = 0                   #total order amount
while complete == 'n':
    products = open("products.txt", 'r')        #opening necessary files
    portions = open("portions.txt", 'r')
    categories = open("categories.txt", 'r')
    
    selection_ = prepareInfo('categories', categories, '')          # first part of order taking, that returns code of next options
    selection_ = prepareInfo('products', products, selection_)      # //
    prepareInfo('portions', portions, selection_)                   
    while True:                                     #checking complete or not
        complete = input('Would you like to complete the order (y/n)?').lower()
        if complete == 'n' or complete == 'y':
            break
print('\n'+ '-' * (50) + '\n')         #printing order recipe
print('Order Recipe')
print('\n'+ '=' * (120) + '\n')
k = 0      
r_line = ''         #each line of order recipe
for x in range(len(order)):
    k += 1
    if k % 4 == 0 :        #there is price data in order 4n in the order list
        total += order[x]       #finding total
        r_line += str(order[x]) + '$'      #convert to string  format for adding line
        print(r_line)           #price info is last element of each line in order recipe
        r_line = ''             #clear r_line for next line
    else : 
        r_line += str(order[x]) + (32-len(order[x]))*' '     #adding datas to line 
print('\n'+ '=' * (120) + '\n')
print('total:   '+ str(format(total, '.2f')) + '$')       #printing total order amount, used format function because sometimes summation's output can be with many decimal