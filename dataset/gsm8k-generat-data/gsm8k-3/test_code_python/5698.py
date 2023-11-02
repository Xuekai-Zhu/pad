def solution():
    """Daria is raising money for a new vacuum cleaner. So far, she has collected $20 in her piggy bank and has decided to put $10 in it each week. If the vacuum cleaner costs $120, how many weeks will it take her to raise enough money to cover this expense?"""
    # Define the initial amount of money Daria has
    starting_amount = 20

    # Define the amount of money Daria adds per week
    weekly_amount = 10

    # Define the cost of the vacuum cleaner
    vacuum_cost = 120

    # Calculate the remaining amount needed to purchase the vacuum cleaner
    remaining_amount = vacuum_cost - starting_amount

    # Calculate the number of weeks needed to raise enough money
    weeks_needed = remaining_amount / weekly_amount

    # Display the number of weeks needed
    result = weeks_needed
    return result

print(solution())