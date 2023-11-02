def solution():
    """During my workout yesterday, I did 30 squats. Each day, I plan to increase my number of squats by 5 more than the previous day. If I do my workout for four consecutive days, how many squats will I perform the day after tomorrow?"""
    starting_squats = 30
    increase_per_day = 5
    squats_on_third_day = starting_squats + (increase_per_day * 2)
    result = squats_on_third_day
    return result

print(solution())