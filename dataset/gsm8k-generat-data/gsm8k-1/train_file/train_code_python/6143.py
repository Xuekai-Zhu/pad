def solution():
    """20 kids in preschool are ready for a nap. 1/2 of the kids fall asleep within the first 5 minutes. Then half of the kids remaining fall asleep within another 5 minutes. How many kids are still awake?"""
    total_kids = 20
    first_round_sleep = total_kids / 2
    remaining_kids = total_kids - first_round_sleep
    second_round_sleep = remaining_kids / 2
    still_awake = remaining_kids - second_round_sleep
    result = still_awake
    return result

print(solution())