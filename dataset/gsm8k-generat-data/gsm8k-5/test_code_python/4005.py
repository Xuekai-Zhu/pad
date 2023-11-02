def solution():
    money_left = 20 - 8 - 4  # Shelby spent $8 on one book and $4 on another
    poster_cost = 4  # Each poster costs $4

    # Calculate the number of posters Shelby can buy with the money she has left
    posters = money_left // poster_cost
    result = posters
    return result

print(solution())