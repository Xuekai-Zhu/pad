def solution():
    """A convenience store sold 100 bags of chips in a month. In the first week, 15 bags of chips were sold. In the second week, thrice as many bags of chips were sold. There was an equal number of chips sold in the third and fourth week. How many chips was each sold in the third and fourth week?"""
    # Define the total number of bags of chips sold and the number of bags sold in the first two weeks
    total_sold = 100
    first_two_weeks = 15 + 3*15

    # Calculate the total number of bags sold in the last two weeks
    last_two_weeks = total_sold - first_two_weeks

    # Since the number of bags sold in the third and fourth week are equal, split the last_two_weeks in half to get the number sold in each week
    third_week = last_two_weeks/2
    fourth_week = last_two_weeks/2

    # Display the number of bags sold in the third and fourth week
    result = (third_week, fourth_week)
    return result

print(solution())