def solution():
    # Calculate the total number of cakes Sara bakes
    total_cakes = 10 * 5

    # Calculate the number of cakes remaining after Carol eats 12
    remaining_cakes = total_cakes - 12

    # Calculate the number of cans of frosting needed to frost the remaining cakes
    cans_of_frosting = remaining_cakes * 2
    result = cans_of_frosting
    return result

print(solution())