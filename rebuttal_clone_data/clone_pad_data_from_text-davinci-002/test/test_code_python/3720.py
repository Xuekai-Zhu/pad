def solution():
    cost_last_year = 85
    cost_this_year = 102
    percent_increase = ((cost_this_year - cost_last_year) / cost_last_year) * 100
    result = percent_increase
    return result

print(solution())