def solution():
    digging_rate = 2  # feet per hour
    initial_digging_time = 4  # hours
    initial_sand_depth = 8  # feet
    washed_away_sand_depth = initial_sand_depth / 2
    tsunami_sand_depth = 2  # feet

    # Calculate the final sand depth
    final_sand_depth = initial_sand_depth - washed_away_sand_depth + tsunami_sand_depth

    # Calculate the time it takes to dig up the treasure with the final sand depth
    digging_time = final_sand_depth / digging_rate

    # Add the initial digging time to the final digging time
    total_digging_time = initial_digging_time + digging_time
    result = total_digging_time
    return result

print(solution())