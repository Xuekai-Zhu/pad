def solution():
    # Distance around the lake
    distance = 15 * 4  # Each side is 15 miles, so the distance around the lake is 4 times 15 miles

    # Speed of swimming
    swim_speed = 1/20  # John can swim 1 mile in 20 minutes, so his swimming speed is 1/20 miles per minute

    # Speed of rowing
    row_speed = 2 * swim_speed # John's rowing speed is twice his swimming speed

    # Time taken to row around the lake
    time = distance / row_speed

    # Convert time to hours
    time_hours = time / 60

    result = time_hours
    return result

print(solution())