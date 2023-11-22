def solution():
    
    # Define the number of scenes drawn per day for each size of scene
    large_scenes_per_day = 5
    medium_scenes_per_day = 6
    small_scenes_per_day = 7

    # Define the number of scenes to be made
    large_scenes = 45
    medium_scenes = 36
    small_scenes = 49

    # Calculate the total number of scenes to be made
    total_scenes = large_scenes + medium_scenes + small_scenes

    # Calculate the total number of days it will take to draw all the scenes
    total_days = total_scenes / (large_scenes_per_day + medium_scenes_per_day + small_scenes_per_day)

    # Display the total number of days
    result = total_days
    return result

print(solution())