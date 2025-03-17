# # #1 Filter function using Lambda
ages = [{"John":25},
        {"Alex":15},
        {"Salim":30},
        {"Jim":12},
        {"Arun":14}]
Under_18 = list(filter(lambda x: list(x.values())[0] < 18, ages))
print(Under_18)

#Map function names above 18 years old
ages = [{"John":25},
        {"Alex":15},
        {"Salim":30},
        {"Jim":12},
        {"Arun":14}]
above_18 = list(map(lambda x: list(x.keys())[0], filter(lambda x: list(x.values())[0] > 18, ages)))
print(above_18)


# #2 Reduce function
from functools import reduce
numbers = [4,5,8,9,3]

product_of_numbers = reduce(lambda x,y: x*y, numbers)
print (product_of_numbers)




#3 Squares of even
numbers = [3,4,5,2,1,8,9]
evens = list(filter(lambda x: x%2 == 0, numbers))
print(evens)

square = evens
square_of_evens = list(map(lambda x: x**2, square))
print(square_of_evens)






#4 To check whether the given string is integer
check_integers = lambda x: x.isdigit()
Enter_letters_or_number = input("")
print(check_integers(Enter_letters_or_number))




#5 Extract the year, month, and day from a datetime object
import datetime
Extract_year_month_date = lambda x: (x.year,x.month,x.day)
Current_datetime = datetime.datetime.now()
year, month, day = Extract_year_month_date(Current_datetime)

print("Year", year)
print("Month", month)
print("Day", day)




#6 To generate a Fibonacci series up to n term
from functools import reduce

n = int(input('Enter the Number of terms'))
def fib(n):
    return reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fib(n))


