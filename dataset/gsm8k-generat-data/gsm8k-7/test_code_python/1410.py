def solution():
    brittney_onions_per_minute = 15 / 5  # 3 onions per minute
    carl_onions_per_minute = 20 / 5  # 4 onions per minute
    brittney_onions_in_30_min = 30 * brittney_onions_per_minute
    carl_onions_in_30_min = 30 * carl_onions_per_minute
    difference = carl_onions_in_30_min - brittney_onions_in_30_min
    result = difference
    return result

print(solution())