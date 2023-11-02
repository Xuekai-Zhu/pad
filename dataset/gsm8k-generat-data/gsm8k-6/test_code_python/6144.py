def solution():
    # Calculate the number of kids remaining awake
    asleep_in_first_5 = 20 * 1/2  # half of the kids fall asleep within the first 5 minutes
    remaining_kids = 20 - asleep_in_first_5  # number of kids remaining awake
    asleep_in_second_5 = remaining_kids * 1/2  # half of the remaining kids fall asleep within another 5 minutes
    still_awake = remaining_kids - asleep_in_second_5  # number of kids still awake
    result = still_awake
    return result

print(solution())