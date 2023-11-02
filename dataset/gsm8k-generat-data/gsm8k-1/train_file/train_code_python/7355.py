def solution():
    """Denmark wants to order pizza. For toppings, he has 3 cheese, 4 meat and 5 vegetable options, one of which is peppers. 
    He can have only one selection from each topping category (one cheese, one meat and one vegetable). However, 
    if he chooses to have pepperoni, he cannot have peppers. How many topping combinations does he have total?"""
    
    # If Denmark has pepperoni, he cannot have peppers
    cheese_options = 3
    meat_options = 4
    vegetable_options = 5
    if "pepperoni" in meat_options:
        vegetable_options = 4
        
    # Calculate total topping combinations
    total_combinations = cheese_options * meat_options * vegetable_options
    
    result = total_combinations
    return result

print(solution())