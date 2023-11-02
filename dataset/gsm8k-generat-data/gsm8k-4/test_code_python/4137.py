def solution():
    """Diego baked 12 cakes for his sister's birthday. Donald also baked 4 cakes, but ate 1 while waiting for the party to start. How many cakes are left?"""
    # Define the initial number of cakes
    initial_cakes = 12 + 4

    # Define the number of cakes that Donald ate
    ate_cakes = 1

    # Calculate the number of remaining cakes
    remaining_cakes = initial_cakes - ate_cakes

    result = remaining_cakes
    return result

print(solution())