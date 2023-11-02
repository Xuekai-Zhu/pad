def solution():
    total_toothbrushes = 330
    january_toothbrushes = 53
    february_toothbrushes = 67
    march_toothbrushes = 46

    # Calculate the total number of toothbrushes remaining after March
    remaining_toothbrushes = total_toothbrushes - january_toothbrushes - february_toothbrushes - march_toothbrushes

    # Calculate the number of toothbrushes given away in April and May
    april_toothbrushes = remaining_toothbrushes / 2
    may_toothbrushes = remaining_toothbrushes / 2

    # Calculate the busiest and slowest months
    busiest_month = max(january_toothbrushes, february_toothbrushes, march_toothbrushes, april_toothbrushes, may_toothbrushes)
    slowest_month = min(january_toothbrushes, february_toothbrushes, march_toothbrushes, april_toothbrushes, may_toothbrushes)

    # Calculate the difference in toothbrushes given out between the busiest and slowest months
    difference = busiest_month - slowest_month
    result = difference
    return result

print(solution())