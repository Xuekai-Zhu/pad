def solution():
    # Define the number of guitar strings Dave breaks per show
    strings_per_show = 2

    # Calculate the number of shows Dave performs
    shows_per_week = 6
    weeks = 12
    total_shows = shows_per_week * weeks

    # Calculate the total number of guitar strings Dave needs to replace
    total_strings_broken = strings_per_show * total_shows
    result = total_strings_broken
    return result

print(solution())