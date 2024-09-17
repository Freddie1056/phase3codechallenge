#function to add two numbers
def Function_add_numbers(num1, num2):
    return num1 + num2


def Number_is_even(num):
    return num % 2 == 0

def To_reverse_string(text):
    return reversed(text)


def count_vowels(a, e, i, o, u):
    count_vowels[a, e, i, o, u]
    count_vowels = count_vowels()

def Calculate_factorial(n):
    if n == 0:
        return 1
    else :return n * Calculate_factorial(n - 1)


def apply_decorator(func):
    def wrapper():
        print("Decorator Applied")
        return func()
    return wrapper

def sort_by_age(tuples_list):
    sorted_list = sorted(tuples_list, key=lambda x: x[1])
    return sorted_list

def merge_dicts(dict1, dict2):
    dict1.update(dict2)
    print(dict1)
    
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print(self.make)  
        print(self.model)  
        print(self.year) 
