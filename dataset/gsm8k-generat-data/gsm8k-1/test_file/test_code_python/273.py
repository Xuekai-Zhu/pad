def solution():
    """It takes Matthew 3 minutes to dig a small hole for shrubs and 10 minutes to dig a large hole for trees. How many hours will it take him to dig 30 small holes and 15 large holes?"""
    time_small_hole = 3
    time_large_hole = 10
    num_small_holes = 30
    num_large_holes = 15
    total_time = (time_small_hole * num_small_holes + time_large_hole * num_large_holes)/60
    result = total_time
    return result

print(solution())