def solution():
    # Calculate the number of bunches of flowers with 9 flowers in each bunch
    initial_bunches = 8
    initial_flowers_per_bunch = 9
    total_initial_flowers = initial_bunches * initial_flowers_per_bunch

    # Calculate the number of bunches of flowers with 12 flowers in each bunch
    new_flowers_per_bunch = 12
    new_bunches = total_initial_flowers // new_flowers_per_bunch

    result = new_bunches
    return result

print(solution())