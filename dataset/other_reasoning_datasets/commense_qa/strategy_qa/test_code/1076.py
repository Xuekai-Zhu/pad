def solution():
    julian_calendar_start = 45
    julian_calendar_end = 1599
    saint_augustine_birth = 354
    saint_augustine_death = 430
    if saint_augustine_birth >= julian_calendar_start and saint_augustine_death <= julian_calendar_end:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())