def solution():
    time_without_brother = 9  # Derek takes 9 minutes to walk a mile without his brother
    time_with_brother = 12  # Derek takes 12 minutes to walk a mile with his brother
    distance = 20  # Derek wants to know how long it would take to walk 20 miles with his brother

    # Calculate the time it would take to walk 20 miles without his brother
    time_without_brother_20_miles = time_without_brother * distance

    # Calculate the time it would take to walk 20 miles with his brother
    time_with_brother_20_miles = time_with_brother * distance

    # Calculate the difference in time
    extra_time = time_with_brother_20_miles - time_without_brother_20_miles
    result = extra_time
    return result

print(solution())