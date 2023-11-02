def solution():
    # Define the speeds on flat sand, downhill slopes, and uphill slopes
    flat_sand_speed = 60
    downhill_speed = flat_sand_speed + 12
    uphill_speed = flat_sand_speed - 18

    # Determine the times spent on each type of slope
    time_on_flat_sand = 1/3
    time_on_downhill_slopes = 1/3
    time_on_uphill_slopes = 1/3

    # Calculate the total distance traveled
    total_distance = 60 * time_on_flat_sand + downhill_speed * time_on_downhill_slopes + uphill_speed * time_on_uphill_slopes

    # Calculate the total time traveled
    total_time = 3

    # Calculate the average speed
    average_speed = total_distance / total_time
    result = average_speed
    return result

print(solution())