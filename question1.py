#question one

#importing the modules
import csv
import re
import random

"""
Helps us find the number in between the parenthese ie; the line number (98)
"""
#creating a utility function to enable in obtaining the line number 
def find_between(text, start, end):
    return re.findall(re.escape(start) + "(.*)" + re.escape(end), text)[0].strip() #to return a list of all matches from the text and remove any space and obtains zero or more occurences. the re.escape() returns all non.alphanumerics backslashed.

"""
Reads the input file then performs the following
1. read one line at a time
2. convert lines that have UVM_INFO, UVM_WARNING, UVM_ERROR into one line
3. extract the fields "message type, full path to file, line number, time, hierarchical location, message" from the rows
4. create a csv with fields "message type, full path to file, line number, time, hierarchical location, message"
https://www.w3schools.com/python/python_file_open.asp
"""

def read_input_file():
    #open the txt file in read mode
    k = open("input1.txt", "r")
    # create a temporary array to store lines that have UVM_INFO, UVM_WARNING, UVM_ERROR
    rows = []

    # read commands in full
    for y in k:
        if "UVM_INFO" in y or "UVM_WARNING" in y or "UVM_ERROR" in y:
            rows.append(y)
        elif rows:
            rows[-1] = rows[-1] + " " + y  #concatenate the last character in row with white space and y

    # extract the data from the commands using the structure
    # <message type> <full path to file>(<line number>) @ <time><timeunit>: <hierarchical location> <message>
    extracted_data = []
    for row in rows:
        try:      # try defines if the block does not contain any errors and without the try block my program will crash and execute an error
            
            first_part = row.split('@')[0].strip() #returns the first part
            last_part = row.split('@')[-1].strip().replace('\n', '') #returns the last part
            message_type = first_part.split(' ', 1)[0] #returns a string
            path = first_part.split(' ', 1)[-1] #returns a string 
            line_number = find_between(first_part, '(', ')') #to find the number in the brackets
            time = last_part.split('ns:')[0] #to return time only
            hl_message = last_part.split('ns:')[-1].strip() #to eliminate the units, i use -1 
            hl = hl_message.split(' ', 1)[0] #to return the full message which is a string not a list
            message = hl_message.split(' ', 1)[-1] # to return the message which is a string not a list
            print(message_type, path, line_number, time, hl, message)
            extracted_data.append([message_type, path, line_number, time, hl, message])
        except Exception as e: #except defines if the statement raises an error
            print(e)
        
    return extracted_data


# https://www.pythontutorial.net/python-basics/python-write-csv-file/
#writing the file in csv
def write_csv(data):
    header = ['message type', 'full path to file', 'line number', 'time', 'hierarchical location', 'message'] #structured order of the header.
    with open(str(random.randint(100000, 999999)) + 'uart_monitor.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f) #to return a delimited string which will later be used in writing the csv file the delimited string is one which is a string representation of data that will be writen in a csv. and to translate every character to binary string using the utf'unicode transformation format'
        # write the header
        writer.writerow(header)#for the header
        for rows in data:
            # write the data
            writer.writerow(rows) #for other rows under the header

def start():
    data = read_input_file()
    write_csv(data)

#adding an input parameter
def correct_number_of_arguments(prompt):
    while True: #to limit repetition
        try:
            rows = int(input(prompt))
        except ValueError:
            print("Sorry, it didn't much.")
        else:
            return rows
