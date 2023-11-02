def solution():
    """Kim's TV uses 125 watts of electricity per hour. She runs it for 4 hours a day. If electricity cost 14 cents per kw/h how many cents does her TV cost to run for a week?"""
    watts_per_hour = 125
    hours_per_day = 4
    days_per_week = 7
    kw_per_day = watts_per_hour * hours_per_day / 1000
    kw_per_week = kw_per_day * days_per_week
    cost_per_kwh = 14
    cost_per_week = kw_per_week * cost_per_kwh
    result = cost_per_week * 100  # cents
    return result

print(solution())