# Data type
nummber = 100 #int it is a whole no that is either positive or negative
second = 56.78 #float it is values with decimal points
text = "Hello there" #string are texts
ispythoninteresting = True #boolean it is whether sth is true or false

# storing multiple values in a variable
cars = ["toyota","nissan","vw"] # a list is changeable
fruits = ("banana","oranges","apples") #Tuple is not changeable
countries = { "kenya","Tanzania","Tunisia","Algeria"} #set
details = {
    "firstname": "Glory",
    "age": 34,
    "course": "web development",
    "nationality": "Kenyan"
} #dictionary
print(details["firstname"])
print(details["age"])
print(second)
print(text)
print(cars)
print(fruits)
print(countries)
print(details)

# Determine a data type
print(type(text))
print(type(countries))
print(type(details))

# Typecasting is converting one data type to another
print(float(nummber))
print(int(second))