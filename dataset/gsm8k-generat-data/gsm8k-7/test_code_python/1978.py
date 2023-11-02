def solution():
    num_days = 5
    morning_distance = 10
    afternoon_distance = 12

    # Calculate the total distance Alice walks in the morning for the whole week
    total_morning_distance = num_days * morning_distance

    # Calculate the total distance Alice walks in the afternoon for the whole week
    total_afternoon_distance = afternoon_distance * (num_days - 1)

    # Add the total morning distance and the total afternoon distance to get the total distance Alice walked in the week
    total_distance = total_morning_distance + total_afternoon_distance
    result = total_distance
    return result

print(solution())