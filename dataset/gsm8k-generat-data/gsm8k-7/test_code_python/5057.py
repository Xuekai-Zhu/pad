def solution():
    num_tomatoes = 21
    num_birds = 2
    fraction_eaten = 1/3

    # Calculate the total number of tomatoes eaten by the birds
    total_eaten = num_birds * fraction_eaten * num_tomatoes

    # Calculate the number of tomatoes left on the plant
    num_left = num_tomatoes - total_eaten
    result = num_left
    return result

print(solution())