# Student ID: 300201041
# by Emre Kesici - 24.12.2023

import os

def create_file(Q):
    identifiers = Q[4].split(',')           #creating a list of users' identifiers
    if 'id' in identifiers:                 #user cannot use 'id' as identifier
        output = 'You cannot create a file with attribute \'id\'.'      
        return output
    else:
        again = False               #conrol variable for output 'line 22-27'
        filename = Q[2] + '.txt'        #making a file name which user mentioned
        if filename in os.listdir():        #checking for 'is there file with same name
            again = True
        file = open(filename, 'w')
        file.write('id')                #id attribute automatically added
        for i in identifiers:
            file.write(',' + i)         #writing on the txt file users attributes
        file.write('\n')
        file.close()
    if again:                           #giving a outtput for condition of 'again'
        output = 'There was already such a file. It is removed and then created again.'
        return output
    else:
        output = 'Corresponding file was successfully created.'
        return output

def delete_file(Q):
    filename = Q[2] + '.txt'          
    if filename not in os.listdir():            #checking if file exist
       output = 'There is no such file.'
       return output
    else:
        os.remove(filename)                     #deleting the file with remove() method
        output = 'Corresponding file was successfully deleted.'
        return output

def display_files(Q):
    files = []                  
    for f in os.listdir():      
        if '.txt' in f:             #find txt file in folder
            files.append(f)          #adding filenames to files list
    display = 'Number of files: ' + str(len(files))         #will be output, first line shows number of files
    count = 0           #for show the file in order
    for filename in files:
        count += 1  
        file = open(filename, 'r')
        line = file.readline()          #to get first line of each file
        display += '\n' + str(count) + ') ' + filename.rstrip('.txt') + ': ' + line.strip('\n')
    return display

def add_line(Q):
    filename = Q[3] + '.txt'
    if filename not in os.listdir():            #checking if file exist
        output = 'There is no such file.'
        return output
    else:
        file = open(filename, 'r')
        line1 = file.readline()
        dataIDs = line1.split(',')              #geting attributes of file
        identifiers = Q[1].split(',')          #get users identifiers from their query
        file.close()
        if len(dataIDs) - 1 != len(identifiers) :       #checking attributes numbers, excluded id, id will automatically added
            output = 'Numbers of attributes do not match.'
            return output
        else:
            file = open(filename, 'r')
            lines = file.readlines()
            lastline = lines[-1]
            forID = (lastline.split(','))[0]
            if forID.isdigit():             #if already there was an id then next id will be 1 more of that
                id_ = int(forID) + 1
            else:                               #if there is only header in file, first lines' id will be 1
                id_ = 1                             
            file.close()
            file = open(filename, 'a')          #appending users' data to file
            nextline = str(id_) + ',' + Q[1]    
            file.write(nextline)
            file.write('\n')
            file.close()
            output = 'New line was successfully added to ' + Q[3] + ' with id = ' + str(id_) + '.'
            return output
            
def remove_lines(Q):
    filename = Q[3] + '.txt'                #checking if file exist
    if filename not in os.listdir():
       output = 'There is no such file.'
       return output
    else:
        file = open(filename, 'r')
        line1 = file.readline()
        identifiers = line1.rstrip('\n').split(',')         #first line of data, (headers)
        identifier = Q[5]                           #users' condition
        file.close()
        if identifier not in identifiers :                  #attribute controls of each user entered attributes
            output = 'Your query contains an unknown attribute.'
            return output
        else:
            new = line1             #for changed file, first line will be same (headers)
            index = identifiers.index(identifier)           #index of user condition identifier
            file = open(filename, 'r')
            lines = file.readlines()
            file.close()
            count = 0               #variable for represent the number of removed lines
            for line in lines[1:]:          #excluded headers
                line_list = line.split(',')
                if Q[6] == '==':            #operator control
                    if line_list[index] != Q[7]:        #If the line that does not satisfy the condition is not added to the new text, 
                        new += line                     #there are no lines that should be deleted that satisfy the condition
                    else:
                        count += 1
                else:
                    if line_list[index] == Q[7]:
                        new += line
                    else:    
                        count += 1
            file = open(filename, 'w')
            file.write(new)         #new text writen on old one
            file.close()
            output = str(count) + ' line(s) were successfully removed.'
            return output

def modify_lines(Q):
    filename = Q[3] + '.txt'
    if filename not in os.listdir():        #checking if file exist
       output = 'There is no such file.'
       return output
    else:
        file = open(filename, 'r')
        line1 = file.readline()
        identifiers = line1.rstrip('\n').split(',')
        identifier1 = Q[1] 
        identifier2 = Q[7]
        file.close()
        if identifier1 not in identifiers or identifier2 not in identifiers :       #attribute controls of each user entered attributes
            output = 'Your query contains an unknown attribute.'
            return output
        elif identifier1 == 'id':               #user not allowed to change id
            output = 'Id values cannot be changed.'
            return output
        else:
            new = line1             #for changed file, first line will be same (headers)
            index1 = identifiers.index(identifier1)         #finding index of users' identifiers on headers
            index2 = identifiers.index(identifier2)
            file = open(filename, 'r')
            lines = file.readlines()        #list of all line
            file.close()
            count = 0                   #variable for represent the number of modified lines
            for line in lines[1:]:      #excluded headers
                line_list = line.split(',')
                if Q[8] == '==':
                    if line_list[index2] != Q[9]:           #if line will not be changed, it will be added same state
                        new += line
                    else:
                        line_list[index1] = Q[5]             #the desired index as a list is replaced with the user's data.   
                        lineprime = ','.join(line_list)         #then it is made a string again with the join() func.
                        new += lineprime                        #and it is added to the new post in that way
                        count += 1
                else:           # '!='
                    if line_list[index2] == Q[9]:
                        new += line
                    else:    
                        line_list[index1] = Q[5]
                        lineprime = ','.join(line_list)
                        new += lineprime
                        count += 1
            file = open(filename, 'w')
            file.write(new)
            file.close()
            output = str(count) + ' line(s) were successfully modified.'
            return output

def fetch_lines(Q):
    filename = Q[3] + '.txt'
    if filename not in os.listdir():            #file exist checking
       output = 'There is no such file.'
       return output
    else:
        file = open(filename, 'r')
        line1 = file.readline()             
        attributes = line1.rstrip('\n').split(',')          #headers of file
        column_list = Q[1].split(',')                   #colums which user wants
        condition = Q[5]                        #users' condition
        file.close() 
        for column in column_list:                          #attribute controls of each user entered attributes
            if column not in attributes:
                output = 'Your query contains an unknown attribute.'
                return output
        if condition not in attributes :
            output = 'Your query contains an unknown attribute.'
            return output

        else:
            columns_len = []
            file = open(filename, 'r')
            lines = file.readlines()
            for attribute in column_list: 
                longestLen = 0                          #variable for specify column length
                for line in lines:
                    word_list = line.rstrip('\n').split(',')             #representing words of each line with for loop
                    word_index = attributes.index(attribute)        #each word have same index with their attributes
                    if longestLen < len(word_list[word_index]) :     #finding longest length of each columns' words 
                        longestLen = len(word_list[word_index])
                columns_len.append(longestLen)           #end of the loop we have ideal lengths of each column, in list with ordered as user entered
            numofstripe = 0                     #variable for outline of table
            
            for stripe in columns_len:          #geting ideal stripe num
                numofstripe += stripe + 3
            numofstripe += 2       #
            stripe_str = numofstripe * '-'
            
            head_columns_str = ''       #first part of fetch table, include headers
            i = -1
            for head in column_list:
                i += 1
                head_columns_str += ('| ' + head + (columns_len[i]-len(head) + 1) * ' ')
            head_columns_str += '|'

            head_columns_prime = ('\n' + stripe_str + '\n'          #------------------
                                  + head_columns_str                #headers
                                  + '\n' + stripe_str )             #------------------
                                   
            fetching_lines_str = ''             #secaond part of table
            count = 0                           #variable for represent num of holded condition
            index = attributes.index(condition)             #finding index of users condition in headers, it will be same index in word_list
            for line in lines[1:]:
                word_list = line.rstrip('\n').split(',')        #all datas of each line                
                if Q[6] == '==':            #operator control
                    if word_list[index] == Q[7]:                #condition control                              
                        fetching_lines_str += '\n'
                        indices = []                            #indices of columns which users' want 
                        for attribute in column_list:
                            word_index = attributes.index(attribute)
                            indices.append(word_index)                  # ^
                        i = -1                              #index value for get right column lenght in columns_length
                        for w in word_list :                            
                            if word_list.index(w) in indices:    #it takes only users mentined column, with using their indices in word_list 
                                word_index = attributes.index(attribute)
                                i += 1                      
                                fetching_lines_str += ('| ' + w + (columns_len[i]-len(w) + 1) * ' ')
                        fetching_lines_str += '|'
                        count += 1

                else:           # '!='
                    if word_list[index] != Q[7]:                        #same
                        fetching_lines_str += '\n'
                        indices = []
                        for attribute in column_list:
                            word_index = attributes.index(attribute)
                            indices.append(word_index)
                        i = -1 
                        for w in word_list :                           
                            if word_list.index(w) in indices:    
                                word_index = attributes.index(attribute)
                                i += 1
                                fetching_lines_str += ('\n| ' + w + (columns_len[i]-len(w) + 1) * ' ')
                        fetching_lines_str += '|'
                        count += 1
                
            if count > 0:                                #if there is hold condition then it print extra line bottom of table
                fetching_lines_str += '\n' + stripe_str

            fetch_txt = ('Number of lines in file students: ' + str(len(lines)-1)       #final output of fetch process
                         +'\nNumber of lines that hold the condition: ' + str(count)
                         + head_columns_prime                         
                         + fetching_lines_str                         )
            return fetch_txt

def main():
    user_input = input('What is your query? (\'x\' to quit)')
    while user_input != 'x':                #
        query = user_input.split(' ')       #making a list with users' query                        

                #then checking query validation
        
        if query[0] == 'create' and query[1] == 'file' and query[3] == 'with' and len(query) == 5 :
            print(create_file(query))
        
        elif query[0] == 'delete' and query[1] == 'file' and len(query) == 3 :
            print(delete_file(query))

        elif query[0] == 'display' and query[1] == 'files' and len(query) == 2 :
            print(display_files(query))

        elif query[0] == 'add' and query[2] == 'into' and len(query) == 4 :
            print(add_line(query))

        elif query[0] == 'remove' and query[1] == 'lines' and query[2] == 'from' and query[4] == 'where' and len(query) == 8 :
            if query[6] == '==' or query[6] == '!=':
                print(remove_lines(query))
            else:
                print('Invalid query.')
        elif query[0] == 'modify' and query[2] == 'in' and query[4] == 'as' and query[6] == 'where' and len(query) == 10 :
            print(modify_lines(query))
        
        elif query[0] == 'fetch' and query[2] == 'from' and query[4] == 'where' and len(query) == 8 :
            print(fetch_lines(query))    

        else:
            print('Invalid query.')

        user_input = input('What is your query? (\'x\' to quit)')

main()
