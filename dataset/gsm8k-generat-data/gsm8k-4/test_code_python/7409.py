def solution():
    """Bill is hoarding toilet paper in fear of another pandemic. Bill goes to the bathroom three times a day and uses 5 squares of toilet paper each time. If Bill has 1000 rolls of toilet paper and each roll has 300 squares of toilet paper, how many days will his toilet paper supply last?"""
    # Define the number of times Bill goes to the bathroom each day, and the number of squares of toilet paper he uses each time.
    bathroom_frequency = 3
    toilet_paper_per_use = 5

    # Define the number of rolls of toilet paper Bill has, and the number of squares of toilet paper on each roll.
    num_rolls = 1000
    squares_per_roll = 300

    # Calculate the total number of squares of toilet paper Bill has.
    total_squares = num_rolls * squares_per_roll

    # Calculate the number of squares used per day.
    squares_used_per_day = bathroom_frequency * toilet_paper_per_use

    # Calculate the number of days Bill's toilet paper supply will last.
    days = total_squares // squares_used_per_day

    result = days
    return result

print(solution())