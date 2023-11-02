def solution():
    watts_per_hour = 125
    hours_per_day = 4
    days_per_week = 7
    cost_per_kw_h = 0.14
    kw_h_per_watt = 1 / 1000
    kw_h_per_day = watts_per_hour * hours_per_day * kw_h_per_watt
    cost_per_day = kw_h_per_day * cost_per_kw_h
    cost_per_week = cost_per_day * days_per_week
    result = cost_per_week
    return result

print(solution())