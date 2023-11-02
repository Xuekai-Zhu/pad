def solution():
    # Calculate the total distance traveled by Tony on the first 4 rollercoasters
    total_distance = (50 + 62 + 73 + 70) * 5/4  # average speed of 59 miles per hour over 5 rollercoasters

    # Calculate the speed of the fifth rollercoaster
    speed_fifth_coaster = ((59 * 5) - total_distance) * 4/1  # distance = speed * time, time = 1 hour
    result = speed_fifth_coaster
    return result

print(solution())