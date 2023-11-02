def solution():
    """Every week of last month Paul tried out a new cake recipe. The first week, he followed a cake recipe that called for 24 cups of sugar. Each week after that, he reduced the amount of sugar by half. How much sugar did he use for the cake on the fourth week?"""
    first_week_sugar = 24
    fourth_week_sugar = first_week_sugar / (2**3)
    result = fourth_week_sugar
    return result

print(solution())