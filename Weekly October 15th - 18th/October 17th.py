#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                     Stacks
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# NOTES
A stack is a data storage technique 
It work like this where the most recent thing you add is also the first to be returned

like this 

currently 1 is in the stack but you add 2 
to return something you pop out from the stack and you will get 2 instead of 1 

since 2 is the most recent addition (by pushing or appending)

This is what a stack looks like 

stack = [1, 2, 3, 4, 5]

^looks like a list right?
Well that's because it is!
The end of the list is the top of stack (like a fallen clock)

okay so append() is how you add data to a stack 

okay so here is the stack

stack = [] #currently empty stack 
stack.append("a")
stack.append("b")
stack.append("c")

print(stack) 

output > ['a', 'b', 'c']

now pop() is the opposite of push and deletes the very top element of the stack (in this case c would be deleted)

stack = [] #currently empty stack 
stack.append("a")
stack.append("b")
stack.append("c")

stack.pop()

print(stack) 

output > ['a', 'b']

CHECKPOINT

stack = [] #currently empty stack 
stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")

stack.pop()

print(stack) 

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                   Challenages
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||

stack = [] #currently empty stack 

first = "r"

second = "t"

third = "s"

fourth = "y"

fifth = "o"

stack.append(third)
stack.append(second)
stack.append(fifth)
stack.append(first)
stack.append(fourth)



print(stack) 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

answer = ["apples", "steak", "potatoes", "carrots"]

response = input("enter a word")

if "s" in response:
    answer.append(response)
    print(answer)
else:
    print("The input doesn't have the letter s")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

answer = ["c", "r", "o", "a", "k"]


answer.pop()
answer.pop()
answer.pop()
answer.pop()

answer.append("o")
answer.append("a")
answer.append("t")

print(answer)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                 Recursion
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# NOTES

Basically a funtion that calls itself

Recursive Santa Claus 
So how are presents delievered? Most people imagine santa going to their house one at a time 

if we were to write code for this it would look like this

houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]

def deliver_presents_iteratively(houses):
    for house in houses:
        print("Delivering presents to", house)

deliver_presents_iteratively(houses)

output > 
Delivering presents to Eric's house
Delivering presents to Kenny's house
Delivering presents to Kyle's house 
Delivering presents to Stan's house

but imagine its like this santa is going to each house and putting in presents! That would take a long time even if he only spent 10 seconds per house it would take years 

so recurisve helps shorten this 

Here is the plan Santa's Recursive Plan

apppoint and elf and give him all the work 

assign titles and responsibilities to the elves based on the number of houses for which they are responsible 

if an elf is responsible for more than one house he is a manager and can divide his work among other elves

if an elf is only repsonible for one house he is a worker who delivers presents to that house 


like this 
elf1 deliver 4 homes
elf2 deliver 2 homes   elf3 deliver 2 homes 
elf4 deliver 1 homes elf5 deliver 1 home elf6 deliver 1 home elf7 deliver 1 home 




here is what that would like in python >

houses = ["Ahmed's house", "Clarks's house", "Xin li's house", "Melissa house"]

#every funtion represents an elf doing their wok 
def deliver_presents_recursively(houses):
    #worker elf doing work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to " + house)

    #manager elf doing work 
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        #divides his work amongst the two else 
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)

CHECKPOINT

this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala']

def feeding(this_list):
    if len(this_list) ==  1:
        this = this_list[0]
        print(f"The {this} has been fed")
    else:
        mid = len(this_list) // 2
        first_half = this_list[:mid]
        second_half = this_list[mid:]
        feeding(first_half)
        feeding(second_half)

feeding(this_list)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                   Challenages
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||

books = [int(n) for n in input("Input a list of numbers").split()]

def total_pages_recursive(books):
    if len(books) == 2:
        book = books[0] + books[1]
        print(book)
    else:
        mid = len(books) // 2
        first_half = books[:mid]
        second_half = books[mid:]
        total_pages_recursive(first_half)
        total_pages_recursive(second_half)

total_pages_recursive(books)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

flowers = [int(n) for n in input("How many blossoms are on each tree?").split()]

def pollinating_recursive(flowers):
    if len(flowers) == 1:
        tree = flowers[0] * 3
        print(tree)
    else:
        mid = len(flowers) // 2
        first_half = flowers[:mid]
        second_half = flowers[mid:]
        pollinating_recursive(first_half)
        pollinating_recursive(second_half)

pollinating_recursive(flowers)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#            Recursion vs Iteration
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#NOTES

iterative is slow going one by one however recursion is way quicker and focuses on efficently!


iterative Factorial
so a commmon way to learn about recusion is to write a facotrial program 

to get a factorial is to multiply all the numbers from 1 to the number 

ex 
1*2*3*4 = 24
one way to get a factorial is to use a iterative process
which would look like this > 

yup = int(input())
def interative_factorial(n):
    results = 1
    for i in range(1, n + 1):
        results *= i
    return results 

print(interative_factorial(yup))

basically it will multiply the amount of yup 
if 4 than 
1*2*3*4  = 24
if 2 than 
1*2 = 2
if 3 than 
1*2*3 = 6 
etc


but what about a recursive factorial? 
def factocial(n):
    if n <= 1:
        return 1
    else:
        return n * (facotrial(n-1))

print(factocial(4))


CHECKPOINT

yuppy = int(input())

def factorial(y):
    if y <= 1:
        return 1 
    else:
        return y * (factorial (y - 1))
    
print(factorial(yuppy))

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                   Challenages
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||

list_of_nums = [int(n) for n in input().split()]

def total(y):
    if len(y) <= 1:
        return y[0]
    else:
        total_sum = 0 
        for num in y:
            total_sum += num
        return total_sum


print(total(list_of_nums))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>