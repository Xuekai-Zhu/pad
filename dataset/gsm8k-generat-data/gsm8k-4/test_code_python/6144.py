def solution():
    """20 kids in preschool are ready for a nap.  1/2 of the kids fall asleep within the first 5 minutes.  Then half of the kids remaining fall asleep within another 5 minutes. How many kids are still awake?"""
    # Define the initial number of kids and calculate how many fall asleep in the first 5 minutes
    initial_kids = 20
    asleep_first_round = initial_kids // 2

    # Calculate how many kids remain awake after the first 5 minutes
    awake_after_first_round = initial_kids - asleep_first_round

    # Calculate how many kids fall asleep in the next 5 minutes
    asleep_second_round = awake_after_first_round // 2

    # Calculate how many kids are still awake
    still_awake = awake_after_first_round - asleep_second_round

    result = still_awake
    return result

print(solution())