def solution():
    # Calculate the total number of sacks of flour in a week
    sacks_per_day = 5
    sacks_per_week = sacks_per_day * 7

    # Calculate the total number of pizza doughs he can make in a week
    doughs_per_sack = 15
    doughs_per_week = sacks_per_week * doughs_per_sack
    result = doughs_per_week
    return result

print(solution())