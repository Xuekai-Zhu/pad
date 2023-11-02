def solution():
    """Every week of last month Paul tried out a new cake recipe. The first week, he followed a cake recipe that called for 24 cups of sugar. Each week after that, he reduced the amount of sugar by half. How much sugar did he use for the cake on the fourth week?"""
    # Define the initial amount of sugar needed
    initial_sugar = 24

    # Calculate the amount of sugar needed for the fourth cake
    fourth_cake_sugar = initial_sugar / (2 ** 3)

    result = fourth_cake_sugar
    return result

print(solution())