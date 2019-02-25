# Exercise 12
print('How many pizzas do you want?')
quantity = int(input())

num_of_pizza = range(1, quantity + 1)
for num in num_of_pizza:
    print('How many toppings for pizza {}?'. format(num))
    num_toppings = int(input())
    print("you want {} of toppings.". format(num_toppings))
