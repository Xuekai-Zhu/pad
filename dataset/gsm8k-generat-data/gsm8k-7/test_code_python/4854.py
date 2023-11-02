def solution():
    fine_per_mph_over_limit = 16
    posted_speed_limit = 50
    total_fine = 256

    # Calculate the number of miles per hour over the posted speed limit that Jed was traveling
    mph_over_limit = total_fine / fine_per_mph_over_limit

    # Calculate the actual speed that Jed was traveling in miles per hour
    actual_speed = posted_speed_limit + mph_over_limit
    result = actual_speed
    return result

print(solution())