def solution():
    walter_fell = 8  # starting platform
    additional_falls = 3  # fell 3 additional depths
    distance_fallen = 4  # distance Walter fell past David

    # Calculate the total distance Walter fell before hitting the ground
    total_distance_fallen = distance_fallen + additional_falls * distance_fallen

    # Calculate the platform heights by dividing the total distance by the number of platforms
    platform_height = total_distance_fallen / (walter_fell + 1)

    # Calculate the height of David's platform by subtracting the distance Walter fell past David
    david_height = platform_height * (walter_fell - 1) - distance_fallen

    # Calculate the platform number based on the height of David's platform
    david_platform = int(david_height / platform_height) + 1

    return david_platform

print(solution())