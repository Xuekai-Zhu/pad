def solution():
    total_days = 5
    total_jerky = 40
    jerky_per_day = 1 + 1 + 2
    jerky_consumed = total_days * jerky_per_day
    jerky_left = total_jerky - jerky_consumed
    jerky_given = jerky_left / 2
    jerky_final = jerky_left - jerky_given
    result = jerky_final
    return result

print(solution())