#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Kafonya Nora
#
# Created:     14/07/2021
# Copyright:   (c) Kafonya Nora 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':

    main()

gender = input("Enter Your Gender")
gender = gender.lower()

age = int(input("Enter your age"))

if gender == "female" and age <=17:
    print("You are a female and you are Welcome")

elif gender == "male" and age <=17:
    print("You are a Male and you are Welcome")

else:
    print("You are not Welcome")

