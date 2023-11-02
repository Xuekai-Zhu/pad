def solution():
    """A frog lays her eggs over a series of 4 days. The first day she lays 50 eggs. The second day, she doubles her production of eggs. The third day she lays 20 more than the second day, and the last day she doubles the first three days total. How many eggs did the frog lay over the span of the 4 days?"""
    # Define the number of eggs laid on each day
    eggs_day1 = 50
    eggs_day2 = eggs_day1 * 2
    eggs_day3 = eggs_day2 + 20
    eggs_day4 = (eggs_day1 + eggs_day2 + eggs_day3) * 2

    # Calculate the total number of eggs laid
    total_eggs = eggs_day1 + eggs_day2 + eggs_day3 + eggs_day4

    # Display the total number of eggs laid
    result = total_eggs
    return result

print(solution())