def solution():
    """The government donated tons of sand to four Cities. City A received 16 1/2 tons of sand, City B received 26 tons of sand, and City C received 24 1/2 tons of sand. The supplier lost the data for City D; however, they know the total for all four cities was 95 tons. How many tons of sand did City D receive?"""
    total_sand = 95
    city_a_sand = 16.5
    city_b_sand = 26
    city_c_sand = 24.5
    city_d_sand = total_sand - city_a_sand - city_b_sand - city_c_sand
    result = city_d_sand
    return result

print(solution())