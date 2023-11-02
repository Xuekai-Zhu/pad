def solution():
    race_distance = 500
    biff_speed = 50  # yards per minute
    kenneth_speed = 51  # yards per minute

    # Calculate the time it takes for Biff to finish the race
    biff_time = race_distance / biff_speed

    # Calculate the distance that Kenneth covers in the same amount of time it takes Biff to finish
    kenneth_distance = kenneth_speed * biff_time

    # Calculate how far past the finish line Kenneth will be when Biff finishes
    past_finish_line = kenneth_distance - race_distance
    result = past_finish_line
    return result

print(solution())