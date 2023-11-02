def solution():
    """Mother made 2 dozen brownies and placed them on the kitchen counter to cool. Father smelled the brownies, came into the kitchen and ate 8 of them. Then, their daughter, Mooney, wandered into the kitchen and ate 4 of the brownies. The next morning, Mother made another two dozen brownies and added them to those remaining from the day before. After that, how many brownies were on the counter?"""
    initial_brownies = 2 * 12
    eaten_brownies = 8 + 4
    remaining_brownies = initial_brownies - eaten_brownies
    total_brownies = remaining_brownies + 2 * 12
    result = total_brownies
    return result

print(solution())