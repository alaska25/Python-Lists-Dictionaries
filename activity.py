# 1. Create a car dictionary with the following keys: brand, model, year of make, color (any values)

# 2. Print the following statement from the details: "I own a (color) (brand) (model) and it was made in (year_of_make)"

# 3. Create a function that gets the square of a number

# 4. Create a function that takes one of the following languages as its parameter:

# a. French
# b. Spanish
# c. Japanese

# Depending on which language is given, the function prints "Hello World!" in that language. Add a condition that asks the user to input a valid language if the given parameter does not match any of the above.


car = {
	"brand": "Toyota",
	"model": "Camry",
	"year of make": "2022",
	"color":"red"
}
print(car.keys())
print(car.values())
print(car.items())

def increaser(num1):
	return lambda num2: num2 * num1

doubler = increaser(2)
print(doubler(3))

def fave_language(language):
	print(f'Hello World, I can speak {language} language!')
fave_language(language="English")
fave_language(language="Spanish")
fave_language(language="Japanese")

