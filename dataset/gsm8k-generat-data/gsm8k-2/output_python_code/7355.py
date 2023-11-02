def solution():
    """Denmark wants to order pizza. For toppings, he has 3 cheese, 4 meat and 5 vegetable options, one of which is peppers. He can have only one selection from each topping category (one cheese, one meat and one vegetable). However, if he chooses to have pepperoni, he cannot have peppers. How many topping combinations does he have total?"""
    cheese_toppings = 3
    meat_toppings = 4
    veg_toppings = 5
    total_combinations = cheese_toppings * meat_toppings * veg_toppings
    # if choosing pepperoni, cannot have peppers
    total_combinations -= meat_toppings
    result = total_combinations
    return result

print(solution())