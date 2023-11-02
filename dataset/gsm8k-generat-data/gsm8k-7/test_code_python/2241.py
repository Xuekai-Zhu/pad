def solution():
    coyote_speed = 15 # mph
    darrel_speed = 30 # mph
    coyote_time = 1 # hour

    # Distance coyote traveled in 1 hour: distance = speed x time
    coyote_distance = coyote_speed * coyote_time

    # Darrel needs to travel the same distance as the coyote to catch up
    # Time = distance / speed
    catch_up_time = coyote_distance / (darrel_speed - coyote_speed)

    result = catch_up_time
    return result

print(solution())