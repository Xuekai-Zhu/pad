def solution():
    time_to_park = 1
    time_to_park_for_mark = time_to_park * 3
    time_rob_leaves = 11
    time_mark_leaves = time_rob_leaves - time_to_park_for_mark
    result = time_mark_leaves
    return result

print(solution())