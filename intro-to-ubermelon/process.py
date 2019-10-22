log_file = open("um-server-01.txt") # pulls file from server


def sales_reports(log_file): #function for the sales report
    for line in log_file:   #initialize for loop through the file
        line = line.rstrip()   #get rid of whitespace in front of the line
        day = line[0:3]  #set variable day to the first 3 characters of the line
        if day == "Mon": #set which day to search for
            print(line)  #print whatever matches the day


sales_reports(log_file)    #runs the function
