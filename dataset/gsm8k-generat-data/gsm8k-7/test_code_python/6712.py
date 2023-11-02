def solution():
    old_shoes_speed = 6  # miles per hour
    hike_duration = 4  # hours

    # Calculate the distance Candace can hike in her old shoes
    old_shoes_distance = old_shoes_speed * hike_duration

    # Calculate the time it takes for Candace to get a blister in her new shoes
    time_per_blister = 2  # hours

    # Calculate the time it takes for Candace to hike in her new shoes before getting a blister
    blister_free_time = 2 * time_per_blister  # 4 hours

    # Calculate the distance Candace can hike without getting a blister in her new shoes
    blister_free_distance = old_shoes_speed * blister_free_time

    # Calculate the speed of Candace after getting a blister in her new shoes
    new_shoes_speed = old_shoes_speed - 2

    # Calculate the time Candace can hike with a blister in her new shoes
    blister_time = hike_duration - blister_free_time

    # Calculate the distance Candace can hike with a blister in her new shoes
    blister_distance = new_shoes_speed * blister_time

    # Calculate the total distance Candace can hike in her new shoes
    new_shoes_distance = blister_free_distance + blister_distance

    result = new_shoes_distance / hike_duration
    return result

print(solution())