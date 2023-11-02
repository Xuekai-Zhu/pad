def solution():
    turns_per_30sec = 6
    num_30sec_in_hour = 120
    num_turns_in_hour = turns_per_30sec * (num_30sec_in_hour/30)
    num_turns_in_two_hours = num_turns_in_hour * 2
    result = num_turns_in_two_hours
    return result

print(solution())