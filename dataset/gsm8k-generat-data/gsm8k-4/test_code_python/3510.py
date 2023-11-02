def solution():
    """Alfred likes to save $1,000.00 over 12 months for his Christmas shopping. He has $100.00 left over from last year's holiday to put towards this year's goal. How much money does Alfred now need to save each month in order to reach his goal in 12 months?"""
    # Define the total savings goal and the amount already saved
    total_goal = 1000
    already_saved = 100

    # Calculate the remaining amount to be saved
    remaining_goal = total_goal - already_saved

    # Calculate the amount to be saved each month
    monthly_goal = remaining_goal / 12

    # return the result
    result = monthly_goal
    return result

print(solution())