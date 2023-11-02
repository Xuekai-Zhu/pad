def solution():
    child_jump_rate = 30  # jumps per minute
    adult_jump_rate = 60  # jumps per minute
    minutes_per_hour = 60
    hours_per_day = 24

    # Calculate the number of jumps per day when Bobby was a child
    child_jumps_per_day = child_jump_rate * minutes_per_hour * hours_per_day

    # Calculate the number of jumps per day now that Bobby is an adult
    adult_jumps_per_day = adult_jump_rate * minutes_per_hour * hours_per_day

    # Calculate the difference in jumps per day between child and adult Bobby
    jump_difference = adult_jumps_per_day - child_jumps_per_day
    result = jump_difference
    return result

print(solution())