def solution():
    """Daria consumes 2.5 times the amount of pizza that Don does. If Don eats 80 pizzas, how many pizzas do they both eat altogether?"""
    # Define the amount of pizza Don eats
    don_pizzas = 80

    # Calculate the amount of pizza Daria eats
    daria_pizzas = don_pizzas * 2.5

    # Calculate the total amount of pizza they both eat
    total_pizzas = don_pizzas + daria_pizzas

    # return the result
    result = total_pizzas
    return result

print(solution())