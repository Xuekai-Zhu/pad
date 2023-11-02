def solution():
    minutes_jogged_per_day = 30
    minutes_jogged_on_Tuesday = minutes_jogged_per_day + 5
    minutes_jogged_on_Friday = minutes_jogged_per_day + 25
    total_minutes_jogged = (minutes_jogged_per_day * 4) + minutes_jogged_on_Tuesday + minutes_jogged_on_Friday
    total_hours_jogged = total_minutes_jogged / 60
    result = total_hours_jogged
    return result

print(solution())