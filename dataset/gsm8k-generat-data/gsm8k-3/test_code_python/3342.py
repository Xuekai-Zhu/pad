def solution():
    """Daria consumes 2.5 times the amount of pizza that Don does. If Don eats 80 pizzas, how many pizzas do they both eat altogether?"""
    # Define the pizza consumption ratio between Daria and Don
    CONSUMPTION_RATIO = 2.5

    # Define the number of pizzas Don eats
    don_pizzas = 80

    # Calculate the number of pizzas Daria eats
    daria_pizzas = don_pizzas * CONSUMPTION_RATIO

    # Calculate the total number of pizzas they both eat
    total_pizzas = don_pizzas + daria_pizzas

    # Display the total number of pizzas
    result = total_pizzas
    return result

print(solution())