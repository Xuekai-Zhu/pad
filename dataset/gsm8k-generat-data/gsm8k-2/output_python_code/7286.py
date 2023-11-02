def solution():
    """Lena has 16 candy bars. She needs 5 more candy bars to have 3 times as many as Kevin, and Kevin has 4 candy bars less than Nicole. How many more candy bars does Lena have than Nicole?"""
    lena_candies = 16
    kevin_candies = lena_candies / 3 - 5
    nicole_candies = kevin_candies + 4
    lena_more_candies = lena_candies - nicole_candies
    result = lena_more_candies
    return result

print(solution())