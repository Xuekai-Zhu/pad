def solution():
    # Calculate the number of tomatoes picked in the first week
    picked_in_first_week = 100 * (1/4)  # Jane picks 1/4 of the 100 tomatoes

    # Calculate the total number of tomatoes picked after two weeks
    picked_in_two_weeks = picked_in_first_week + 20 + (2 * 20)  # Jane picks 20 more in the second week and twice that in the third week

    # Calculate the number of tomatoes remaining on the plant
    tomatoes_remaining = 100 - picked_in_two_weeks
    result = tomatoes_remaining
    return result

print(solution())