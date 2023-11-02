def solution():
    total_hours = 8
    fraction_lilly = 1/4
    fraction_fiona = 1 - fraction_lilly
    hours_lilly = total_hours * fraction_lilly
    hours_fiona = total_hours * fraction_fiona
    minutes_fiona = hours_fiona * 60
    result = minutes_fiona
    return result

print(solution())