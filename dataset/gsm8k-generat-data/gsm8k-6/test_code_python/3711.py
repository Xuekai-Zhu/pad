def solution():
    # Calculate the number of pears Katherine has
    num_pears = 3 * 4  # Katherine has 3 times as many pears as apples

    # Calculate the total number of fruits Katherine has
    total_fruits = 4 + num_pears + num_bananas  # Katherine has 4 apples, num_pears pears, and num_bananas bananas

    # Calculate the number of bananas Katherine has
    num_bananas = 21 - total_fruits  # Katherine has a total of 21 fruits, so subtract the number of apples and pears from 21 to get the number of bananas

    result = num_bananas
    return result

print(solution())