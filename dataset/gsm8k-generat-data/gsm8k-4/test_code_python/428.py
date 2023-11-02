def solution():
    """A frog lays her eggs over a series of 4 days. The first day she lays 50 eggs. The second day, she doubles her production of eggs. The third day she lays 20 more than the second day, and the last day she doubles the first three days total. How many eggs did the frog lay over the span of the 4 days?"""
    # Define the number of eggs laid on the first day
    eggs_first_day = 50

    # Calculate the number of eggs laid on the second day
    eggs_second_day = eggs_first_day * 2

    # Calculate the number of eggs laid on the third day
    eggs_third_day = eggs_second_day + 20

    # Calculate the total number of eggs laid on the first three days
    eggs_first_three_days = eggs_first_day + eggs_second_day + eggs_third_day

    # Calculate the total number of eggs laid on the fourth day
    eggs_fourth_day = eggs_first_three_days * 2

    # Calculate the total number of eggs laid over the span of the four days
    total_eggs = eggs_first_day + eggs_second_day + eggs_third_day + eggs_fourth_day

    # return the result
    result = total_eggs
    return result

print(solution())