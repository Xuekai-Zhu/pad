def solution():
    # Define the initial number of chickens
    initial_chickens = 4

    # Double the number of chickens
    doubled_chickens = initial_chickens * 2

    # Subtract one, due to the dog eating a chicken
    remaining_chickens = doubled_chickens - 1

    # Add the final group of chickens
    final_chickens = 4 + 10 - 4

    # Add all the chickens together
    total_chickens = remaining_chickens + final_chickens
    result = total_chickens
    return result

print(solution())