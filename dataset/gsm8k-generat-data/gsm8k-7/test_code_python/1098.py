def solution():
    num_watermelons = 30
    num_weeks = 0

    while num_watermelons > 0:
        num_weeks += 1
        num_watermelons -= 3
        num_watermelons -= 2

    result = num_weeks
    return result

print(solution())