def solution():
    """Denmark wants to order pizza. For toppings, he has 3 cheese, 4 meat and 5 vegetable options, one of which is peppers. He can have only one selection from each topping category (one cheese, one meat and one vegetable). However, if he chooses to have pepperoni, he cannot have peppers. How many topping combinations does he have total?"""
    # Define the number of options for each topping
    num_cheeses = 3
    num_meats = 4
    num_veggies = 5

    # Define whether or not peppers are an option
    peppers = True

    # If Denmark has pepperoni, he cannot have peppers
    if peppers:
        num_veggies -= 1

    # Calculate the total number of topping combinations
    total_combinations = num_cheeses * num_meats * num_veggies

    # Return the result
    result = total_combinations
    return result

print(solution())