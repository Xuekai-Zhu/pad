def solution():
    rob_time = 1  # time it takes for Rob to get to the park
    mark_time = rob_time * 3  # time it takes for Mark to get to the park

    # Calculate the time at which Mark should leave his home
    mark_leave_time = 11 + (rob_time + mark_time) / 2

    result = mark_leave_time
    return result

print(solution())