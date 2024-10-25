#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                   Bubble Sort
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#notes 

Sorting algorithms that are useful for sorting data!
Bubble sort is one of these algorithms 
Used to sort list into numerical order
basically comparing the two adjacent numbers and if necessary sawpping them 

ONLY WORKS WITH NUMBER INFORMATION 
does not work with strings 

at the end of each iteration the largest number is added to the top of the list and the algorithm repeats 

Pseudocode is a way to write concept program without a specfic language 

here is the Pseudocode for this program(being bubble sort)

funtion BubbleSort(list)
    for all elements in list:
        if list[i] > list[i+1]
            wap(list[i], list[i+1])
        end if
    end for
    return list
end BubbleSort

python ver

def BubbleSort(my_list):
    n = len(my_list)
    
    for i in range(n):  
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

Check point  #))))))))))))))))))))))))))))))))))))))

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
choice = int(input("Enter random number"))
arr.append(choice)

def BubbleSort(my_list):
    n = len(my_list)
    
    for i in range(n):  
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    
    return my_list


BubbleSort(arr)

print(arr)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                Selection Sort
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#notes 
so another algorithm 

basically selecting the smallest value in the list and placing it at the beginning of the list (does this obviously until its numericaly sorted)

it creates two list the orginal unsorted and the new sorted 


here is Pseudocode code

funtion SelectionSort(list)

    for all elements (i) in list:
        minimum = i
        for remaining elements (j) in list:
            if list[j] < list[minimum]:
                minimum = j
            end if
        end for
        if the index of minimum ! = i:
            swap list[minimum] and list[i]
        end if
    end for
    return list
end SelectionSort 


python ver 

def selection_sort(my_list):
    n = len(my_list)
    
    for i in range(n):
        minimum_index = i
        
        for j in range(i+1, n):
            if my_list[j] < my_list[minimum_index]:
                minimum_index = j
        
        if minimum_index != i:
            my_list[i], my_list[minimum_index] = my_list[minimum_index], my_list[i]
    
    return my_list

Check point #))))))))))))))))))))))))))))))))))))))

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

choice = int(input("enter in a number"))

arr.append(choice)


def selection_sort(my_list):
    n = len(my_list)
    
    for i in range(n):
        minimum_index = i
        
        for j in range(i+1, n):
            if my_list[j] < my_list[minimum_index]:
                minimum_index = j
        
        if minimum_index != i:
            my_list[i], my_list[minimum_index] = my_list[minimum_index], my_list[i]
    
    return my_list

print(selection_sort(arr))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                Insertion Sort
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#notes  

now here is insertion sorting 

similar to selection sort it basically takes the next unsorted value and inserts it into its correct place in the sorted list 

here is the Pseudocode 

funtion InsertionSort(list):
    insert-sort = 0 
    val_to_insert = 0

    for all elements (i) in list:
        val_to_insert = list[i]
        insert_spot = i
    
    while insert_spot > 0 and list[insert_spot-1] > val_to_insert
        list[insert_spot] = list[insert_spot - 1]
        insert_spot = insert_spot - 1
    end while

    list[insert_spot] = val_to_insert
    end for
    return list
end InsertionSort


python ver 
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        val_to_insert = my_list[i]
        insert_spot = i

        while insert_spot > 0 and my_list[insert_spot - 1] > val_to_insert:
            my_list[insert_spot] = my_list[insert_spot - 1]
            insert_spot -= 1

        my_list[insert_spot] = val_to_insert

    return my_list


Check point #))))))))))))))))))))))))))))))))))))))
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
choice = int(input("enter number"))

arr.append(choice)


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        val_to_insert = my_list[i]
        insert_spot = i

        while insert_spot > 0 and my_list[insert_spot - 1] > val_to_insert:
            my_list[insert_spot] = my_list[insert_spot - 1]
            insert_spot -= 1

        my_list[insert_spot] = val_to_insert

    return my_list

print(insertion_sort(arr))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                Merge Sort
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#notes  

basically uses recursion (calling it own funtion when needed)

it splts the list into half and again and again until their is only one element 
it then merges the sublist (numerical order)
and does this again and again until it the orginal list but sorted 


here is the Pseudocode
answer = int(input("Enter a number 0 - 100"))
arr = [1,0,5,6,7,8,11,2,55,66,77,34,67,23]
arr.append(answer)

def mergeSort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list)//2
        L = sort_list[:mid]
        R = sort_list[mid:]
        mergeSort(L)
        merge(R)

        i = j = k = 0

    while i < len(L) and j < lend(R):
        if L[i] < R[j]:
            sort_list[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L)
        sort_list[k] = l[i]
        i += 1
        k += 1
    
    while j < len(R):
        sort_list[k] = R[j]
        j += 1
        k += 1

mergeSort(arr)
print(arr)


python ver

def mergeSort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2 
        L = sort_list[:mid]
        R = sort_list[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sort_list[k] = L[i]
                i += 1
            else:
                sort_list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            sort_list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            sort_list[k] = R[j]
            j += 1
            k += 1

    return sort_list

Check point #))))))))))))))))))))))))))))))))))))))
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
choice = int(input("enter number"))

arr.append(choice)

def mergeSort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2 
        L = sort_list[:mid]
        R = sort_list[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                sort_list[k] = L[i]
                i += 1
            else:
                sort_list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            sort_list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            sort_list[k] = R[j]
            j += 1
            k += 1

    return sort_list

print(mergeSort(arr))
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                   Challenages
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>