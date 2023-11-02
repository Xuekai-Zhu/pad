def solution():
    # Define the variables
    starting_amount = 0
    donated_amount = 0
    hot_dog_cost = 2
    remaining_amount = 55

    # Calculate the donated amount
    donated_amount = starting_amount / 2

    # Calculate the amount spent on the hot dog
    remaining_amount -= hot_dog_cost

    # Calculate the amount left over
    remaining_amount -= donated_amount

    # Calculate the starting amount
    starting_amount = remaining_amount * 2

    result = starting_amount
    return result

print(solution())