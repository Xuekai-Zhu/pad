def solution():
    """Denmark wants to order pizza.  For toppings, he has 3 cheese, 4 meat and 5 vegetable options, one of which is peppers. He can have only one selection from each topping category (one cheese, one meat and one vegetable). However, if he chooses to have pepperoni, he cannot have peppers. How many topping combinations does he have total?"""
    # Define the number of options for each topping category
    CHEESE_OPTIONS = 3
    MEAT_OPTIONS = 4
    VEGETABLE_OPTIONS = 5

    # Define the number of options for the vegetable topping category if peppers are chosen
    NO_PEPPERS_VEGETABLE_OPTIONS = VEGETABLE_OPTIONS - 1

    # Calculate the total number of topping combinations
    total_combinations = CHEESE_OPTIONS * MEAT_OPTIONS * NO_PEPPERS_VEGETABLE_OPTIONS

    # Display the total number of topping combinations
    result = total_combinations
    return result

print(solution())