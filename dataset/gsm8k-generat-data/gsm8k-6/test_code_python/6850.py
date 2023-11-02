def solution():
    # Calculate the total number of guitar strings that Dave needs to replace
    strings_per_week = 2 * 6  # Dave breaks 2 guitar strings per night when playing live, and performs 6 shows a week
    total_strings = strings_per_week * 12  # Dave performs for 12 weeks
    result = total_strings
    return result

print(solution())