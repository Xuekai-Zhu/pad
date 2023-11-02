def solution():
    # Define the coyote's speed and the time it has been traveling
    coyote_speed = 15
    coyote_time = 1

    # Calculate the distance the coyote has traveled
    coyote_distance = coyote_speed * coyote_time

    # Calculate Darrell's speed and the time it will take to catch up to the coyote
    darrell_speed = 30
    darrell_time = coyote_distance / (darrell_speed - coyote_speed)

    result = darrell_time
    return result

print(solution())