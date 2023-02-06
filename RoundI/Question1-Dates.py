from datetime import datetime

def is_date_format_correct(date:str)->bool:
    """
    This function takes in a date in string format
    and returns true if the date matches the format
    YYYY-MM-DD and false if it doesn't
    """

    #your code here#
    
    #Initializing format
    format = "%Y-%m-%d"

    #checking if the format matches the date
    res = True

    #using try-except to check for the truth value
    try:
        res = bool(datetime.strptime(date,format))
    except ValueError:
        res = False

    return res
 
#Asks the user to input date in string format "YYYY-MM-DD" and stores it in variable date_string.
date = input("Enter date in  string format(YYYY-MM-DD): ")

#Printing results
print("Does date match format?",str(is_date_format_correct(date)))

