def solution():
    strings_per_night = 2
    shows_per_week = 6
    weeks = 12

    # Calculate the total number of strings that Dave will break in 12 weeks
    total_strings_broken = strings_per_night * shows_per_week * weeks

    result = total_strings_broken
    return result

print(solution())