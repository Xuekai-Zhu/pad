def solution():
    coyote_speed = 15  # Coyote is traveling east at 15 miles per hour
    darrel_speed = 30  # Darrel is traveling east at 30 miles per hour
    initial_time_difference = 1  # Animal left footprints 1 hour ago

    # Calculate the distance between Darrel and the coyote when Darrel starts chasing
    initial_distance = coyote_speed * initial_time_difference

    # Calculate the time it will take for Darrel to catch up to the coyote
    catching_time = initial_distance / (darrel_speed - coyote_speed)
    result = catching_time
    return result

print(solution())