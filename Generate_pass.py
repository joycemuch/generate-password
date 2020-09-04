import random
import string

def user():
    return input("Generate a pass , choose ( weak , strong , very strong): ")

def len():
    return (input("password length :"))

def key_gen():
     lists=["weak" , "strong" , "very strong"]
     key = user()
     while key not in lists:
         print("enter the correct keyword")
         key =  user()
     else:
        key_len = int(len())
        if key == lists[0]:
            key_list = random.sample(string.digits,key_len)
            print( "".join(key_list))
        elif  key == "strong":
                key_list = random.sample(string.ascii_lowercase+string.ascii_uppercase, key_len)
                print( "".join(key_list))
        elif key == "very strong":
            key_list = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits+ string.punctuation,key_len)
            print( "".join(key_list))
     return 
key_gen()