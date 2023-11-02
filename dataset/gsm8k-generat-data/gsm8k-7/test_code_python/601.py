def solution():
    cheetah_speed = 60  # miles per hour
    gazelle_speed = 40  # miles per hour
    distance_apart = 210  # feet
    miles_per_hour_to_feet_per_second = 1.5 * 5280 / 3600  # converts mph to fps

    # Calculate the relative speed of the cheetah to the gazelle in feet per second
    relative_speed = (cheetah_speed - gazelle_speed) * miles_per_hour_to_feet_per_second

    # Calculate how long it would take the cheetah to catch up to the gazelle, in seconds
    time_to_catch_up = distance_apart / relative_speed
    result = time_to_catch_up
    return result

print(solution())