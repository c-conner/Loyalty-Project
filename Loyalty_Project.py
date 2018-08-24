import time
import sys

#One main issue with this program will be to check if somone has inputted the same email. 
#i could have another text file with just emails....

def list_of_customers(string): # This function prints out the current customers
    with open(string, 'r') as file:
        names = file.read()
        print(names)

def customer_list(name): # This function appends the names to  a text file named 'names.txt'
    with open('names.txt', 'a') as file:
        file.write(name)

def customer_information(name): # This function appends the information to a text file named 'information.txt'
    with open('information.txt', 'a') as file:
       file.write(name)

def loyalty_modification(email, information): # This function reads the file and write over the line that starts with the email entered.
    with open('information.txt', 'r+') as file:
        for line in file:
            if line.startswith(email):
                line.replace(line, information)
            break

def checking(email): # This function checks to see if the email argument is within the text file. If it is, the information from the line is returned
    with open ('information.txt', 'r') as file:
        for line in file:
            if line.startswith(email):
                information = line
                break
            else:
                information = None
        return information

        

def yes_or_no(answered):# This function check to see if the user answered yes or no.
   while answered != 'yes' and answered != 'no':
       time.sleep(0.50)
       print("Type 'yes' or 'no'")
       answered = input()
   return answered 


def check_name(value):# if i have time, i should add middle initial
    value_1 = len(value.split())
    while value_1 != 2:
        print("A first and last name is needed (Make sure there is a space inbetween your first and last name.)")
        time.sleep(0.50)
        value = input('What is your first & last name?')
        value_1 = len(value.split())
    return value 

def check_email(value_2):
    checking = 0
    numbers = len(value_2.split())
    while checking != 1:
        while '@' not in value_2:
            print("You could have aleast put an @ sign in your 'email.'")
            time.sleep(0.50)
            value_2 = (input('What is your email?'))
            checking = .50
        while numbers != 1:
             print("Emails do not have spaces in them....")
             value_2 = (input('What is your email?'))
             numbers = len(value_2.split())
             checking += .50
        checking = 1
    return value_2
        
# I should ask them if they want to be apart of the Loyalty points thingy...
if __name__ == "__main__":
    print("Welcome to 'The Store', and thankyou for purchasing our item(s).")
    time.sleep(0.50)
    print("Here are the customers that are apart of our 'loyalty program'.")
    list_of_customers('names.txt')
    response = yes_or_no(input("Do you want to take part the loyalty program? Type 'yes' or 'no'").lower())
    if response == 'no':
        print('Have a great day.')
        sys.exit()
    print("Great! Are you a new customer?") 
    time.sleep(1.50)
    answer = yes_or_no(input("Type 'yes' or 'no'").lower())
    if answer == 'yes':
        answer_1 = check_name(input('What is your first & last name?'))
        answer_2 = check_email(input('What is your email?'))
        Loyalty_Points = 10
        time.sleep(0.50)
        print(f"Thankyou for signing up with 'Loyalty Points'. You have {Loyalty_Points} loyalty points.")
        time.sleep(0.50)
        print('Comeback again!')
        customer_information(f"{answer_2} {answer_1} {Loyalty_Points}\n")
        customer_list(f"name:{answer_1} email:{answer_2}\n")
        sys.exit()
    elif answer == 'no':
        print('We just need to check to see if you are in our file.')
        answer_1 = check_name(input('What is your first & last name?'))
        answer_2 = check_email(input('What is your email?'))
        info = checking(answer_2)
        if info == None:
            print('Sorry, the information you gave is invalid...Goodbye.')
            sys.exit()
        else:
            split_information = info.split()
            previous_points = int(split_information[3]) 
            first_last_name = f'{split_information[1]} {split_information[2]}'
            email = f'{split_information[0]}'
            Loyalty_Points = int(split_information[-1]) + 10
            time.sleep(0.50)
            print(f'We have added 10 more points to your current loyalty points.\nYou now have {Loyalty_Points} loyalty points, {first_last_name}.')
            updated_information = f'{email} {first_last_name} {Loyalty_Points}'
            print(f"This is your updated information:{updated_information}")
    if Loyalty_Points >= 30:
        print(f"You have {Loyalty_points} loyalty points, would you like some candy? ")
        answer = yes_or_no(input("It's only 30 loyalty points.(Type 'yes' or 'no')").lower())
        if answer == 'no':
            loyalty_modification(email, updated_information)
            time.sleep()
            print('Have a great day.')
            sys.exit()
        elif answer == 'yes':
            Loyalty_Points -= 30 
            updated_information = f'{email} {first_last_name} {Loyalty_Points}'
            print('Take a candy of your choice....')
            loyalty_modification(email, updated_information)
            time.sleep(0.50)
            print(f'This is your updated information:{updated_information}') #need to update my file...
            time.sleep(0.50)
            print('Have a great day.')
            sys.exit()
    else:
        loyalty_modification(email, updated_information)
        time.sleep(0.50)
        print('Once you have 30 loyalty points we will offer you a candy of your choice.\nHave a great day.')