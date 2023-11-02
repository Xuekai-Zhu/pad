def solution():
    starting_chickens = 4
    additional_chickens = starting_chickens
    dog_loss = 1
    found_chickens = 4 < 10

    # Double the number of starting chickens
    total_chickens = starting_chickens * 2

    # Subtract 1 for the chicken lost to the dog
    total_chickens -= dog_loss

    # Add the number of chickens found
    total_chickens += found_chickens

    result = total_chickens
    return result  # Return the final answer

print(solution())