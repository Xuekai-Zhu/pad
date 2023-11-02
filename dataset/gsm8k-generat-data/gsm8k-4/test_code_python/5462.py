def solution():
    """Ann can skate 6 miles an hour. Her friend Glenda can skate 8 miles an hour. If they start in the same place and skate in straight lines in opposite directions for 3 hours, how many miles apart do they end up?"""
    # Define Ann and Glenda's skating speeds
    ann_speed = 6
    glenda_speed = 8

    # Calculate Ann and Glenda's distances traveled
    ann_distance = ann_speed * 3
    glenda_distance = glenda_speed * 3

    # Calculate the total distance they end up apart
    total_distance = ann_distance + glenda_distance

    # return the result
    result = total_distance
    return result

print(solution())