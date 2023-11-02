def solution():
    """On Rudolph's car trip across town, he traveled 2 more than 5 miles and encountered 3 less than 17 stop signs. How many stop signs per mile did Rudolph encounter on his trip across town?"""
    # Define the number of miles traveled and the number of stop signs encountered
    miles = 5 + 2
    stop_signs = 17 - 3

    # Calculate the number of stop signs per mile
    stop_signs_per_mile = stop_signs / miles

    # return the result
    result = stop_signs_per_mile
    return result

print(solution())