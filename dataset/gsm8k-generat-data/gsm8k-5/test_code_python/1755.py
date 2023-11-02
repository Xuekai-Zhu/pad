def solution():
    original_distance = 150  # John's normal trip is 150 miles
    original_time = 3  # John's normal trip would take 3 hours
    extra_distance = 50  # John drives an extra 50 miles

    # Calculate the new distance and time
    new_distance = original_distance + (2 * extra_distance)  # John has to go 50 miles out of the way and then back to the route
    new_time = (new_distance / original_distance) * original_time  # John still maintains the same speed

    result = new_time
    return result

print(solution())