# try block test code for error
# except block code runs to see if error happens
# else block code run if no error happens 
# finally block code runs regardless of try/except blocks



#when there is a problem an exception block is displayed 
#so like this 

#try:
    #print(greeting)
#except:
    #print("A problem occured")

#greeting = "Hello"
#try:
   # print(greeting)
#except:
   # print("problem")
#else:
    #print("the code worked") #else block if no error #MUST COME AFTER ECEPT BLOCK IS OP

#greeting = "Hello"
#try:
    #print(greeting)
#except:
    #print("problem")
#else:
    #print("the code worked")
#finally:
    #print("Your exception is complete") #runs no matter what 

#slice_p = int(input("how many slices of pizza?"))
#numberofpeople = int(input("how many people?"))

num_sun = int(input("number of sunflowers"))


try:
    print(num_sun*300)
except:
    print("There is a problem")
else:
    print("There is no problem")
finally:
    print("Your exception handling is complete")