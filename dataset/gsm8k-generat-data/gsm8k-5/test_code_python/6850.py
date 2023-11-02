def solution():
    strings_per_night = 2  # Dave breaks 2 guitar strings per night
    shows_per_week = 6  # Dave performs 6 shows per week
    weeks = 12  # Dave performs for 12 weeks

    # Calculate the total number of guitar strings Dave will need to replace
    total_strings = strings_per_night * shows_per_week * weeks
    result = total_strings
    return result

print(solution())