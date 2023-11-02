def solution():
    distance = 600
    speed = 50
    initial_time = distance / speed

    # To decrease travel time by 4 hours, the new travel time would be initial_time - 4.
    new_time = initial_time - 4

    # Calculate the new speed needed to cover the distance in the new time.
    new_speed = distance / new_time

    # Calculate the increase in speed needed to achieve the new speed
    increase_in_speed = new_speed - speed

    result = increase_in_speed
    return result

print(solution())