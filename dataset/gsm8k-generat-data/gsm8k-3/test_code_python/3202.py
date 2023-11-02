def solution():
    """Milly's babysitter charges $16/hour. Milly is considering switching to a new babysitter who charges $12/hour, but also charges an extra $3 for each time the kids scream at her. If Milly usually hires the babysitter for 6 hours, and her kids usually scream twice per babysitting gig, how much less will the new babysitter cost?"""
    # Define the hourly rate and scream fee for the new babysitter
    NEW_RATE = 12
    NEW_SCREAM_FEE = 3

    # Get the number of hours Milly hires the babysitter for
    hours = 6

    # Get the number of times Milly's kids scream during each babysitting gig
    screams = 2

    # Calculate the cost of the old babysitter
    old_cost = hours * 16

    # Calculate the cost of the new babysitter
    new_cost = hours * NEW_RATE + screams * NEW_SCREAM_FEE

    # Calculate the difference in cost between the old and new babysitters
    cost_difference = old_cost - new_cost

    # Display the cost difference
    result = cost_difference
    return result

print(solution())