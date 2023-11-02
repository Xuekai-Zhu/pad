def solution():
    red_with_spots = 2/3 * 12  # Two-thirds of the red mushrooms have white spots
    brown_with_spots = 6  # All of the brown mushrooms have white spots
    blue_with_spots = 1/2 * 6  # Half of the blue mushrooms have white spots

    # Calculate the total number of mushrooms with white spots
    total_with_spots = red_with_spots + brown_with_spots + blue_with_spots
    result = total_with_spots
    return result

print(solution())