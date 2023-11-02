def solution():
    """TreShawn's mom needs to order pizza for her son and his two friends. She knows that TreShawn always eats 1/2 a pizza. His friend Michael eats 1/3 of a pizza and his other friend LaMar eats 1/6 of a pizza. How many pizzas does she need to order?"""
    # Calculate the total amount of pizza needed
    total_pizza = 1/2 + 1/3 + 1/6

    # Round up to the nearest integer to account for ordering a whole pizza
    total_pizza = round(total_pizza) 

    result = total_pizza
    return result

print(solution())