def solution():
    """John manages to run 15 mph for his whole 5-mile race. The next fastest guy ran the race in 23 minutes. How many minutes did he win the race by?"""
    john_time = (5/15) * 60
    next_fastest_time = 23
    time_difference = john_time - next_fastest_time
    result = time_difference
    return result

print(solution())