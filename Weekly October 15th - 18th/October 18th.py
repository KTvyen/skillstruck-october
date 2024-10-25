#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#            Recursion vs Iteration
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                   Challenages
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||

#pt2

number = int(input("Enter a number: "))

def fibonacci(num):
    if num == 0:
        return [0]
    elif num == 1:
        return [0, 1]
    else:
        fib_seq = fibonacci(num - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Call the function to generate the Fibonacci sequence
fibonacci_list = fibonacci(number - 1)  # Adjusted to get 'number' elements

print(fibonacci_list)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#            Recursion vs Iteration
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#NOTES
bubble sorting 
selection sorting 
insertionsorting 
merge sorting 

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                   Challenages
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>