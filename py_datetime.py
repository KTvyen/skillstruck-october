import datetime

#birth = int(input("What month are you born? (1 - 12): "))

#x = datetime.datetime.now()
#current_month = int(x.strftime("%m"))
#days_left_in_month = 10


#if 1 <= birth <= 12:
    #if birth >= current_month:
        #months_until_birthday = birth - current_month
    #else:
       # months_until_birthday = (12 - current_month) + birth

  #  print(f"You have {months_until_birthday} months and #{days_left_in_month} days until it's your birthday month!")
#else:
   # print("Please enter a valid month between 1 and 12.")



x = datetime.datetime.now()


month_pass = int(x.strftime("%m")) - 1
day_pass = int(x.strftime("%d"))

print(f"It has been {month_pass} months and {day_pass} days since your New Years resolution. How are you doing?")