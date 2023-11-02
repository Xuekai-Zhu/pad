def solution():
    ivy_stripped_per_day = 6
    ivy_growth_per_night = 2
    total_ivy = 40
    days_to_strip = total_ivy / ivy_stripped_per_day + (total_ivy % ivy_stripped_per_day)
    result = days_to_strip
    return result

print(solution())