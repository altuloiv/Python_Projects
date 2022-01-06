

class User: ####Parent Class ###
    name = 'No Name Provided'
    email = ' '
    password = '123abcd'
    account_number = 0

class Employee(User): #######Child Class 1#####
    base_pay = 11.00
    department = 'General'

class Customer(User): ######child Class 2######
    mailing_address = ''
    mailing_list = True