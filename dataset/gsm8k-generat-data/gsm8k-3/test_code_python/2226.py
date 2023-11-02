def solution():
    """Every week of last month Paul tried out a new cake recipe.  The first week, he followed a cake recipe that called for 24 cups of sugar. Each week after that, he reduced the amount of sugar by half. How much sugar did he use for the cake on the fourth week?"""
    # Define the initial amount of sugar
    initial_sugar = 24

    # Calculate the amount of sugar used in the fourth week
    sugar_4 = initial_sugar / (2 ** 3)

    # Display the amount of sugar used in the fourth week
    result = sugar_4
    return result

print(solution())