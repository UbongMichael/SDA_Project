
# # # ##################################################################################################
# # # #
# # #
# # #
# # # def money_change(pounds):
# # #     pounds = 1.09 * euro
# # #     return pounds
# # #
# # # pound1 = float(input("Please enter the first pound value. "))
# # # print(pound1, type(pound1))
# # #
# # # pound2 = float(input("dearest sir or madam, please specify the number or quantity of pound you'd like ti exchange for euro. "))
# # # print(pound2, type(pound2))
# # #
# # #
# # # outputMessage  = " The equivalent value in euro is : "
# # # print(f"You're exchanging {pound1} for {money_change(pound1)}")
# # # print (outputMessage + str(money_change(pound2))
# # #
# # # # print (euros, type(euro)))
# #
# #

# #
# #



# #
# #
# # # 1. Money change
# # # Write a function called money_change
# # # that takes an amount of money in English pounds as its parameter,
# # # converts it into euros and returns the result (currency exchange rate: 1 GBP = 1.09 EUR).
# # # Call this function at least twice in the program; at least one of the calls must be based on the data asked from the user). Output the results in euros.
# #
# # # Example of the function call:
# #
# # #  >>>money_change(150.6)
# # #  164.154
# # # Example of the program output:
# #
# # #  Please enter the amount of money in English pounds: 80
# # #  This is 87.2 EUR
# # #  500 GBP is 545.0 EUR
# #
# # # general format for a function definition:
# # # def functionName(input parameters):
# # # DON'T FORGET THE COLON
# #
# # # function definition
# # def money_change(pounds):
# #     # thanks, Python
# #     euros = 1.09 * pounds
# #     return euros
# #
# #
# # pounds1 = float(input("Please enter the first pound value."))
# # print(pounds1, type(pounds1))
# # pounds2 = float(input(
# #     "Dearest sir or madam, please specify the number or quantity of pounds you'd like to exchange for euros. Thank you."))

# # print(pounds2, type(pounds2))
# # outputMessage = "The equivalent value in euros is: "
# # print(f"You're exchanging {pounds1} for {money_change(pounds1)}")
# # print(outputMessage + str(money_change(pounds2)))
# #
# #
# # # function calls
# # # money_change(someValue1)
# # # money_change(someValue2)
# #
# # #################################################################
# #
# #
# # def money_change_2(pounds):
# #     # thanks, Python
# #     euros = 1.09 * pounds
# #     print(f"The number of pounds you gave me is: {pounds}")
# #     print("The number of euros is: ", euros, type(euros))
# #     return euros
# #
# #
# # money_change_2(34345.5656)
# #
# # # the variablese euros and pounds only have function scope and cannot be called or referenced outside of the function
# # # print(euros, type(euros))
# # # print(pounds, type(pounds))
# #
#
# # print(money_change_2(34345.5656), type(money_change_2(34345.5656)))
#
#
#
# def name_month(number):
#     if int(number) == 1:
#         print("January")
#     if int(number) == 2:
#         print("February")
#     if int(number) == 3:
#         print("March")
#     if int(number) == 4:
#         print("April")
#     if int(number) == 5:
#         print("May")
#     if int(number) == 6:
#         print("June")
#     if int(number) == 7:
#         print("July")
#     if int(number) == 8:
#         print("August")
#     if int(number) == 9:
#         print("September")
#     if int(number) == 10:
#         print("October")
#     if int(number) == 11:
#         print("November")
#     if int(number) == 12:
#         print("December")
#
# number = input("Enter the number of the month: ")
# #name_month(number)
#
#
# # function definition here
# # assume the user enters integer values for date, month and year
# def date_as_string(day, month, year): # date, month and year are parameters; also known as arguments
#     if month == 1:
#         monthName = "January"
#     if month == 2:
#         monthName = "February"
#     if month == 3:
#         monthName = "March"
#     if month == 4:
#         monthName = "April"
#     if month == 5:
#         monthName = "May"
#     if month == 6:
#         monthName = "June"
#     if month == 7:
#         monthName = "July"
#     if month == 8:
#         monthName = "August"
#     if month == 9:
#         monthName = "September"
#     if month == 10:
#         monthName = "October"
#     if month == 11:
#         monthName = "November"
#     if month == 12:
#         monthName = "December"
#     print(f"{monthName} {day}, {year}")
# # function call below
# # date_as_string(1, 1, 2021)
# ######################################
# # Then write a program that asks the user to enter a day, a month and a year in numbers,
# # and the program outputs the corresponding date as a string.
# # want output in the form January 1, 2021
# day = input("Enter the number of the day: ")
# month = int(input("Enter the number of the month: "))
# year = input("Enter the number of the year: ")
# date_as_string(day, month, year)


##########################################################################################################
# def hello_world(words):
#     size = max(len(word) for word in words)
#     print("*"*(size+4))
#
#     for i in words:
#         print("*"+" "+i+" "*((size+4)-len(i)-3)+"*")
#
#     print("*"*(size+4))
#
# hello_world(["Hello","world","in","a","frame"])



#########################################################################################################
# Python program to check if year is a leap year or not
year = 2000

 # To get year (integer input) from the user
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
