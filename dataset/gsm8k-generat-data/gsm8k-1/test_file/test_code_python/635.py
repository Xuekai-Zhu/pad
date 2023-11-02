def solution():
    """Bob wants to dig a hole 6 feet long by 4 feet wide by 3 feet deep. If it takes him 3 seconds to shovel a cubic foot of earth, how long will it take him to dig the hole?"""
    length = 6
    width = 4
    depth = 3
    volume = length * width * depth
    time_per_cubic_feet = 3
    total_time = volume * time_per_cubic_feet
    result = total_time
    return result

print(solution())