import random
import time
import array

#max length of password
max_len = 8
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
           'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z']

up_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
              'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
              'Z']


print("Hi! welcome to password generator.")
word = input("Name a word or a letter and i will convert it into a cool password: ")
time.sleep(1)
if word == "":
    print("Sorry! please try again!")
else:
    combined = digits + letters + up_letters + list(word)
    rand_digit = random.choice(digits)
    rand_upper = random.choice(up_letters)
    rand_lower = random.choice(letters)
    temp_pass = rand_digit + word + rand_upper + rand_lower
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
            password = password + x          
    # print out password
    print(password)
    input('press enter to exit \n -made by MagmaStuff.')
