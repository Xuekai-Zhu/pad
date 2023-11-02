def solution():
    # Calculate the number of lemons Cristine has left after giving some to her neighbor
    lemons_bought = 12  # Cristine bought a dozen lemons
    lemons_given = lemons_bought * (1/4)  # Cristine gave 1/4 of the lemons to her neighbor
    lemons_left = lemons_bought - lemons_given  # calculate the lemons left
    result = lemons_left
    return result

print(solution())