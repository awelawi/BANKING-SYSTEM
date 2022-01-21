"""Attempt at creating a banking system without OOP"""
from re import S
from xml.etree.ElementTree import tostring
import permutation
import random

# def toString(List):
#     """This is called backtracking algorithm"""
#     return "".join(List)
# def pssblPerm(string, l, r):
#     if l == r:
#         print(toString(string))
#     else:
#         for i in range(l, r+1):
#             string[i], string[l] = string[l], string[i]
#             pssblPerm(string, l+1, r)
#             string[i], string[l] = string[l], string[i]
    
# string = "0123456789"
# liststr = list(string)
# lenstr = len(string) - 1
# y = pssblPerm(liststr, 0, lenstr)
# print(y)

# def userdetails():
#     """Users bio details"""
#     print("Welcome to Ella's mobile banking app! Fast and safe cash transactions")
#     first_name = input("Hi there!, what's your first name: ")
#     last_name = input("What's your last name: ")
#     gender = input("What's your gender?: ")
#     state= input("What state are you from?: ")
#     country = input("What country are you from?: ")
#     email_address = input("What's your email address?: ")
#     phone_number= input("What's your phone number?: ")
#     print("Thank you for filling this information correctly, your account number will be generated shortly")
#     accountlist = permutation.accountperm()
#     computerrandom = random.choice(accountlist)
#     print(f"Your account number is {computerrandom}, ensure you keep it!")
#     return [(first_name, last_name, gender, state, country, email_address, phone_number, computerrandom)]
    # return list(tupledir)
# print(userdetails())
# def works(first_name, last_name, gender, state, country, email_address, phone_number, computerrandom):
#     """checks if it works"""
# field = userdetails()
# print(field)
# # print(field)
# def uppercase(listdir):
#     """Returns the entire string in uppercase"""
#     for i in range(len(listdir)):
#         listdir[i] = listdir[i].upper()
    # return listdir
# vari = userdetails()
# print(uppercase(vari))

# def checkstrings(string):
#     while string != str(string):
        


