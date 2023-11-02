def solution():
    flat_sand_speed = 60  # Dune buggy speed on flat sand
    downhill_speed = flat_sand_speed + 12  # Dune buggy speed on downhill slopes
    uphill_speed = flat_sand_speed - 18  # Dune buggy speed on uphill slopes
    time_on_each_surface = 1 / 3  # Conner spends one-third of the time on each surface

    # Calculate the weighted average speed of the dune buggy
    average_speed = (flat_sand_speed * time_on_each_surface) + (downhill_speed * time_on_each_surface) + (
            uphill_speed * time_on_each_surface)
    result = average_speed
    return result

print(solution())