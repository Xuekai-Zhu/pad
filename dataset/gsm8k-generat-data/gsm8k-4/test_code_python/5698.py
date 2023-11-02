def solution():
    """Daria is raising money for a new vacuum cleaner. So far, she has collected $20 in her piggy bank and has decided to put $10 in it each week. If the vacuum cleaner costs $120, how many weeks will it take her to raise enough money to cover this expense?"""
    # Define the initial amount and the amount to be added each week
    initial_amount = 20
    weekly_amount = 10

    # Define the cost of the vacuum cleaner
    vacuum_cleaner_cost = 120

    # Calculate the number of weeks it will take to save enough money
    weeks = (vacuum_cleaner_cost - initial_amount) / weekly_amount

    # Round up the number of weeks to the nearest whole number
    weeks = int(weeks) + 1

    # Return the result
    result = weeks
    return result

print(solution())