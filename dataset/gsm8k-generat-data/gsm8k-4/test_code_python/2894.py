def solution():
    """Ian spent half the money he made on doing online surveys. If he worked 8 hours doing surveys and on average he's able to earn $18 per hour doing surveys, how much money does he have left?"""
    # Define the number of hours worked and the hourly rate
    hours_worked = 8
    hourly_rate = 18

    # Calculate the total earnings from doing online surveys
    total_earnings = hours_worked * hourly_rate

    # Calculate the amount of money Ian spent
    amount_spent = total_earnings / 2

    # Calculate the amount of money Ian has left
    amount_left = total_earnings - amount_spent

    # return the result
    result = amount_left
    return result

print(solution())