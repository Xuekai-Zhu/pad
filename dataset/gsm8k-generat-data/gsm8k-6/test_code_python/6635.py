def solution():
    # Calculate the total number of apples given away
    apples_given = 25 - 3  # Sarah had three apples left when she got home
    apples_given -= 5  # Sarah gave a single apple to each of her 5 closest friends
    apples_given -= (number_of_teachers * 1)  # Sarah gave an apple to each teacher she saw
    result = apples_given
    return result

print(solution())