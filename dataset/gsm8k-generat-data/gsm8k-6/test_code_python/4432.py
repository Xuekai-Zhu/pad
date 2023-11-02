def solution():
    # Calculate the total number of days in February
    days_in_Feb = 28
    # Calculate the number of days in January
    days_in_Jan = 31
    # Calculate the total number of photos taken in January
    photos_in_Jan = 2 * days_in_Jan
    # Calculate the total number of photos taken in February
    photos_in_Feb = 146 - photos_in_Jan
    # Calculate the number of photos taken each week in February
    photos_per_week = photos_in_Feb / (days_in_Feb / 7)
    result = photos_per_week
    return result

print(solution())