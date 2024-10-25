#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                 Objects Continued
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# NOTES

Is a tool for programming 
Uses Objects and classes 

A quick reveiw on what a class looks like / what it is

notice the color and capitalization!
init has two of _ <-- those on each side 
all classes start with that self, 
and they must be defined! 

Rememeber a class is like the blue print it isn't actually the house it just helps defines what needs to go into making it!

class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

But that now what about creating a object? 
To do that set a variable with a name 
I choosing pet 

Set that = to the class and than define the name, age, and gender of the pet

Notice how the terms are in qoutes

pet = Dog("Jasmine", "15", "Female")

print(pet) 

That above is an object! ^^

We can further add to it using this code *adding attribute not changeing value btw

call the variable and the attribute and than set the ne attribute 

pet.height = 12

now the new object looks like -->

Jasmine 15 Female 12

But what to do when you want to remove a attribute? 

Well use this code > 

delattr(name) 

However to change a value use this code

pet.name = "Franz"

similar to the adding attribute one before but using one that has already been defined

The Inverse of this is to delete a value of course 


Use this simple code here >

del pet.name

Now unlike before their is still a name attribute but no value. Trying to print the attribute now will encor an error 

You can also add funtions to the classes 
(Those funtions in classes are called methods)

class Dog:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender = gender 
    def greating(self):
        print("Good Morning")

pet = Dog("Jasmine", "15", "Female")
pet.greeting()

now if you run this code the output will be 
Good Morning 

basically the object used that funtion [when you did this pet.greeting()]

check point >

class Vacation:
    def __init__(self, place, distance, weather):
        self.place = place
        self.distance = distance
        self.weather = weather 
    def tuesday(self):
        print("We will be hiking on Tuesday.")

summer = Vacation("Hawaii", 2000, "Sunny")
summer.tuesday()
summer.rating = 10
summer.weather = "rainy"

print(summer)
print(summer.rating)
print(summer.weather)


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                   Challenages
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||


class Friday:
    def __init__(self, activity, friend):
        self.activity = activity
        self.friend = friend
    def pictures(self):
        print("We took so many pictures!")

thisWeekend = Friday("Movie", "Charlotte")

thisWeekend.money = 20

thisWeekend.friend = "Shane"

print(thisWeekend)
print(thisWeekend.money)
print(thisWeekend.friend)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Shopping:
   
	def __init__(self, item, quality):
		self.item = item
		self.quality = quality
		self.total = []
		
	def spending(self, cost):
		self.total.append(cost)

sportStore = Shopping("Kayak", "High Quality")

sportStore.spending(17)
sportStore.spending(20)
sportStore.spending(40)

print(sportStore.total)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

