def solution():
    cheese_toppings = 3
    meat_toppings = 4
    vegetable_toppings = 5
    pepperoni = 1
    peppers = 1
    total_combinations = cheese_toppings * meat_toppings * vegetable_toppings - pepperoni - peppers
    result = total_combinations
    return result

print(solution())