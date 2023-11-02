def solution():
    total_kids = 20  # There are 20 kids in preschool

    # Calculate the number of kids that fall asleep within the first 5 minutes
    asleep_first_round = total_kids // 2

    # Calculate the number of kids remaining after the first round
    remaining_kids = total_kids - asleep_first_round

    # Calculate the number of kids that fall asleep within the second 5 minutes
    asleep_second_round = remaining_kids // 2

    # Calculate the number of kids still awake
    still_awake = total_kids - asleep_first_round - asleep_second_round
    result = still_awake
    return result

print(solution())