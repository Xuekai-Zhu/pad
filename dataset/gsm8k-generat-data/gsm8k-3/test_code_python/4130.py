def solution():
    """Kyle can lift 60 more pounds this year, which is 3 times as much as he could lift last year. How many pounds can Kyle lift in all?"""
    # Define the increase in weight from last year to this year
    increase = 60

    # Calculate how much Kyle could lift last year
    last_year = increase / 3

    # Calculate how much Kyle can lift in all
    total_weight = last_year + increase

    # Display the total weight Kyle can lift
    result = total_weight
    return result

print(solution())