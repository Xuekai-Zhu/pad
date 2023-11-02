def solution():
    toothbrushes_given_away = [53, 67, 46]
    busiest_month = max(toothbrushes_given_away)
    slowest_month = min(toothbrushes_given_away)
    difference = busiest_month - slowest_month
    result = difference
    return result

print(solution())