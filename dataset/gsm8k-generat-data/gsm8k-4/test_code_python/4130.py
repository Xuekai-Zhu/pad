def solution():
    """Kyle can lift 60 more pounds this year, which is 3 times as much as he could lift last year. How many pounds can Kyle lift in all?"""
    # Define the weight Kyle could lift last year
    last_year_lift = None

    # Define the weight Kyle can lift this year
    this_year_lift = last_year_lift * 3 + 60

    # Calculate the total weight Kyle can lift
    total_lift = last_year_lift + this_year_lift

    # return the result
    result = total_lift
    return result

Note: The solution is incomplete as the value of last_year_lift is missing.

print(solution())