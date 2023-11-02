def solution():
    # Calculate the total hours slept by Angela in December and January
    hours_slept_December = 6.5 * 31  # assuming December has 31 days
    hours_slept_January = 8.5 * 31  # assuming January also has 31 days

    # Calculate the difference in hours slept between January and December
    extra_hours = hours_slept_January - hours_slept_December
    result = extra_hours
    return result

print(solution())