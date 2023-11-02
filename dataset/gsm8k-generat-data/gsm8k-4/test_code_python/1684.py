def solution():
    """A convenience store sold 100 bags of chips in a month. In the first week, 15 bags of chips were sold. In the second week, thrice as many bags of chips were sold. There was an equal number of chips sold in the third and fourth week. How many chips was each sold in the third and fourth week?"""
    # Define the total number of bags of chips sold in the first two weeks
    chips_sold_first_two_weeks = 15 + 3*15

    # Define the total number of bags of chips sold in the last two weeks
    chips_sold_last_two_weeks = 100 - chips_sold_first_two_weeks

    # Calculate the number of bags of chips sold in each of the last two weeks
    chips_sold_per_week = chips_sold_last_two_weeks // 2

    # Return the result
    result = chips_sold_per_week
    return result

print(solution())