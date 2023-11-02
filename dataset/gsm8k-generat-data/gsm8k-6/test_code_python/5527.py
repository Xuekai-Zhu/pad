def solution():
    # Calculate the total distance Walter fell
    total_distance_fallen = 4 + 3*4  # Walter fell past David after falling 4 meters, and fell an additional three times that depth before hitting the ground

    # Calculate the height of each platform
    height_per_platform = total_distance_fallen / 8  # there were 8 platforms in total

    # Calculate the platform David was on
    height_David_on = total_distance_fallen - 4  # David was immediately below where Walter fell past him
    platform_David_on = height_David_on // height_per_platform  # round down to the nearest platform
    result = platform_David_on
    return result

print(solution())