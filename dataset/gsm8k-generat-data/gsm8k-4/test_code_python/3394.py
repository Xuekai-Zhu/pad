def solution():
    """The government donated tons of sand to four Cities. City A received 16 1/2 tons of sand, City B received 26 tons of sand, and City C received 24 1/2 tons of sand. The supplier lost the data for City D; however, they know the total for all four cities was 95 tons. How many tons of sand did City D receive?"""
    # Define the total amount of sand donated
    total_sand = 95

    # Calculate the amount of sand received by City D
    city_d_sand = total_sand - (16.5 + 26 + 24.5)

    # Return the result
    result = city_d_sand
    return result

print(solution())