def solution():
    # Calculate the difference in Bobby's jumping ability as a child and as an adult
    child_jumps_per_minute = 30  
    adult_jumps_per_minute = 60  # since adult Bobby can jump 1 jump per second, or 60 jumps per minute
    difference = adult_jumps_per_minute - child_jumps_per_minute
    result = difference
    return result

print(solution())