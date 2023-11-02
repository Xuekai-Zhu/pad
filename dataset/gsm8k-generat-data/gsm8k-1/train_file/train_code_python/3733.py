def solution():
    """Jerry is making cherry syrup. He needs 500 cherries per quart of syrup. It takes him 2 hours to pick 300 cherries and 3 hours to make the syrup. How long will it take him to make 9 quarts of syrup?"""
    cherries_per_quart = 500
    cherries_needed = cherries_per_quart * 9
    time_to_pick = 2
    time_to_make = 3
    total_time = time_to_pick + time_to_make
    time_needed = total_time * ((cherries_needed / 300) // 1)
    if (cherries_needed % 300) > 0:
        time_needed += total_time
    result = time_needed
    return result

print(solution())