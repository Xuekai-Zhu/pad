def solution():
    """Lauren is a cartoonist. She can draw 5 large-sized picture scenes per day, or she can draw 6 medium-sized picture scenes per day, or she can draw 7 small-sized picture scenes per day. She was hired for a big project to create 45 large-sized picture scenes, 36 medium-sized picture scenes, and 49 small-sized picture scenes. How many days will it take for her to create all of the picture scenes?"""
    large_scenes_per_day = 5
    medium_scenes_per_day = 6
    small_scenes_per_day = 7
    num_large_scenes = 45
    num_medium_scenes = 36
    num_small_scenes = 49

    days_for_large = num_large_scenes / large_scenes_per_day
    days_for_medium = num_medium_scenes / medium_scenes_per_day
    days_for_small = num_small_scenes / small_scenes_per_day

    total_days = days_for_large + days_for_medium + days_for_small
    result = total_days
    return result

print(solution())