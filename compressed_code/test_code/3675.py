def solution():
    
    total_toothbrushes = 330
    january_toothbrushes = 53
    february_toothbrushes = 67
    march_toothbrushes = 46
    remaining_toothbrushes = total_toothbrushes - january_toothbrushes - february_toothbrushes - march_toothbrushes
    april_toothbrushes = remaining_toothbrushes / 2
    may_toothbrushes = remaining_toothbrushes / 2

    busiest_month = max(january_toothbrushes, february_toothbrushes, march_toothbrushes, april_toothbrushes, may_toothbrushes)
    slowest_month = min(january_toothbrushes, february_toothbrushes, march_toothbrushes, april_toothbrushes, may_toothbrushes)
    result = busiest_month - slowest_month
    return result

print(solution())