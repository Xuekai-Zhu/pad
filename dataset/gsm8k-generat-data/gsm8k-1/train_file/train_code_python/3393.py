def solution():
    """The government donated tons of sand to four Cities. City A received 16 1/2 tons of sand, City B received 26 tons of sand, and City C received 24 1/2 tons of sand. The supplier lost the data for City D; however, they know the total for all four cities was 95 tons. How many tons of sand did City D receive?"""
    total_sand = 95
    sand_a = 16.5
    sand_b = 26
    sand_c = 24.5
    sand_d = total_sand - (sand_a + sand_b + sand_c)
    result = sand_d
    return result

print(solution())