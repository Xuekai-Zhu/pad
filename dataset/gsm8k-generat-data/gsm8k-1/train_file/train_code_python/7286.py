def solution():
    """Lena has 16 candy bars. She needs 5 more candy bars to have 3 times as many as Kevin, and Kevin has 4 candy bars less than Nicole. How many more candy bars does Lena have than Nicole?"""
    lena_candy = 16
    kevin_candy = (lena_candy - 5) / 3
    nicole_candy = kevin_candy + 4
    lena_more = lena_candy - nicole_candy
    result = lena_more
    return result

print(solution())