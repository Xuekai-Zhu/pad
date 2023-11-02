def solution():
    # Calculate the distance around the lake
    distance_around = 4 * 15

    # Calculate John's swim speed
    swim_speed = 1 / (20/60)  # miles per hour

    # Calculate John's row speed
    row_speed = 2 * swim_speed

    # Calculate the time it takes to row around the lake
    time_to_row = distance_around / row_speed  # in hours

    result = time_to_row
    return result

print(solution())