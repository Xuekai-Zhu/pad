def solution():
    people = 30
    times_failed = people // 6
    times_double = people // 10
    times_single = people - times_failed - times_double
    result = times_double + times_single
    return result

print(solution())