def solution():
    """The government donated tons of sand to four Cities. City A received 16 1/2 tons of sand, City B received 26 tons of sand, and City C received 24 1/2 tons of sand. The supplier lost the data for City D; however, they know the total for all four cities was 95 tons. How many tons of sand did City D receive?"""
    # Calculate the total tons of sand received by cities A, B, and C
    total_ABC = 16.5 + 26 + 24.5

    # Calculate the tons of sand received by City D
    city_D = 95 - total_ABC

    # Display the tons of sand received by City D
    result = city_D
    return result

print(solution())