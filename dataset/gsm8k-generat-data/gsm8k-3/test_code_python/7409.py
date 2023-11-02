def solution():
    """Bill is hoarding toilet paper in fear of another pandemic. Bill goes to the bathroom three times a day and uses 5 squares of toilet paper each time. If Bill has 1000 rolls of toilet paper and each roll has 300 squares of toilet paper, how many days will his toilet paper supply last?"""
    # Define the number of times Bill goes to the bathroom per day and the number of squares of toilet paper he uses each time
    bathroom_per_day = 3
    squares_per_use = 5

    # Define the number of squares of toilet paper per roll and the number of rolls that Bill has
    squares_per_roll = 300
    rolls = 1000

    # Calculate the total number of squares of toilet paper that Bill has
    total_squares = squares_per_roll * rolls

    # Calculate the number of squares of toilet paper that Bill uses per day
    daily_use = bathroom_per_day * squares_per_use

    # Calculate the number of days that Bill's toilet paper supply will last
    days = total_squares // daily_use

    # Display the number of days
    result = days
    return result

print(solution())