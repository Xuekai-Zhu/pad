def solution():
    shots_blocked_first_period = 4  # Jordan blocked 4 shots in the first period
    shots_blocked_second_period = 2 * shots_blocked_first_period  # Jordan blocked twice as many shots in the second period
    shots_blocked_third_period = shots_blocked_second_period - 3  # Jordan blocked three fewer shots in the third period than in the second
    total_shots_blocked = 21  # Jordan blocked a total of 21 shots in all periods

    # Calculate the number of shots blocked in the fourth period
    shots_blocked_fourth_period = total_shots_blocked - (shots_blocked_first_period + shots_blocked_second_period + shots_blocked_third_period)
    result = shots_blocked_fourth_period
    return result

print(solution())