def solution():
    # Define the initial bunch and flower counts
    initial_bunches = 8
    initial_flowers = 9

    # Calculate the number of flowers in the new bunch
    new_flowers = 12

    # Calculate the new number of bunches
    new_bunches = (initial_bunches * initial_flowers) / new_flowers

    result = new_bunches
    return result

print(solution())