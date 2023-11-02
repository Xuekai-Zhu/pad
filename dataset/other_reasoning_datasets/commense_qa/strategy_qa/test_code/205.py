def solution():
    night_shift_hours = range(23, 8)
    telescope_hours = range(0, 24)
    overlap = [hour for hour in telescope_hours if hour in night_shift_hours]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())