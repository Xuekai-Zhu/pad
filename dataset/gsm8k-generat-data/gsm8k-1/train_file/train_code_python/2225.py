def solution():
    """Every week of last month Paul tried out a new cake recipe. The first week, he followed a cake recipe that called for 24 cups of sugar. Each week after that, he reduced the amount of sugar by half. How much sugar did he use for the cake on the fourth week?"""
    initial_sugar = 24
    week_four_sugar = initial_sugar / (2**3) # dividing by 2 for each week
    result = week_four_sugar
    return result

print(solution())