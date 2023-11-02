def solution():
    # Calculate the number of shirts Kendra needs to have to last for two weeks
    shirts_per_week = 5 + 3 + 1 + 2  # Kendra wears 5 shirts to school, changes 3 times for club, wears 1 shirt on Saturday and 2 on Sunday
    shirts_per_two_weeks = shirts_per_week * 2  # multiply by 2 to get shirts for two weeks
    result = shirts_per_two_weeks
    return result

print(solution())