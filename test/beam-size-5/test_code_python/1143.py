def solution():
    
    large_scenes_per_day = 5
    medium_scenes_per_day = 6
    small_scenes_per_day = 7
    num_large_scenes = 45
    num_medium_scenes = 36
    num_small_scenes = 49
    total_scenes = (num_large_scenes * large_scenes_per_day) + (num_medium_scenes * medium_scenes_per_day) + (num_small_scenes * small_scenes_per_day)
    days_to_draw_all_scenes = total_scenes / total_scenes
    result = days_to_draw_all_scenes
    return result

print(solution())