def solution():
    hours_short_show = 0.5
    hours_long_show = 1
    episodes_short_show = 24
    episodes_long_show = 12
    total_hours = (hours_short_show * episodes_short_show) + (hours_long_show * episodes_long_show)
    result = total_hours
    return result

print(solution())