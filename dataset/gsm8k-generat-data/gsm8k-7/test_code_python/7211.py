def solution():
    ivy_coverage = 40  # in feet
    ivy_strip_per_day = 6
    ivy_growth_per_night = 2

    total_days = 0
    remaining_ivy = ivy_coverage

    while remaining_ivy > 0:
        total_days += 1
        remaining_ivy -= ivy_strip_per_day
        if remaining_ivy > 0:
            remaining_ivy += ivy_growth_per_night

    result = total_days
    return result

print(solution())