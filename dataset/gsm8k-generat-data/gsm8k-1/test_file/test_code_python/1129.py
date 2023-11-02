def solution():
    """Grandma walks 3 miles every day on her favorite walking trail, which includes 2 miles of walking on the beach and 1 mile of walking on the sidewalk. On the sidewalk, Grandma walks at twice the rate of speed that she does on the beach. If 40 minutes of her walk is spent on the beach, how long does it take for her to complete the entire 3-mile walk, in minutes?"""
    beach_distance = 2
    sidewalk_distance = 1
    beach_speed = 1
    sidewalk_speed = 2 * beach_speed
    beach_time = 40/60  # convert minutes to hours
    sidewalk_time = sidewalk_distance / sidewalk_speed
    total_time = beach_time + sidewalk_time + beach_time  # add beach time again to get total time
    result = total_time * 60  # convert back to minutes
    return result

print(solution())