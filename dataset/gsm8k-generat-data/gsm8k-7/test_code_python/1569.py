def solution():
    lake_side_length = 15
    swimming_speed = 1/20  # miles per minute
    rowing_speed = swimming_speed * 2  # miles per minute

    # Calculate the distance around the lake
    lake_distance = lake_side_length * 4

    # Calculate the time it takes to row around the lake
    rowing_time = lake_distance / rowing_speed  # minutes
    rowing_time = rowing_time / 60  # hours
    result = rowing_time
    return result

print(solution())