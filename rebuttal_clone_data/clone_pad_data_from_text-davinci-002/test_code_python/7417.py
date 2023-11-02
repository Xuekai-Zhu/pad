def solution():
    max_rate = 2
    max_time = 30
    zach_rate = 3
    zach_time = 40
    num_balloons_popped = 10
    total_balloons_filled = ((max_rate * max_time) + (zach_rate * zach_time)) - num_balloons_popped
    result = total_balloons_filled
    return result

print(solution())