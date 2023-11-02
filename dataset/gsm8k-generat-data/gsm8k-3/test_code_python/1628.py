def solution():
    """TreShawn's mom needs to order pizza for her son and his two friends. She knows that TreShawn always eats 1/2 a pizza. His friend Michael eats 1/3 of a pizza and his other friend LaMar eats 1/6 of a pizza. How many pizzas does she need to order?"""
    # Define the fraction of a pizza each person eats
    TRESHAWN = 1/2
    MICHAEL = 1/3
    LAMAR = 1/6

    # Calculate the total fraction of pizza needed
    total_fraction = TRESHAWN + MICHAEL + LAMAR

    # Calculate the total number of pizzas needed
    total_pizzas = total_fraction / (1/1) # convert fraction to whole pizza

    # Display the total number of pizzas needed
    result = total_pizzas
    return result

print(solution())