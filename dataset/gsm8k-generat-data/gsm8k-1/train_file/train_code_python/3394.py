def solution():
    """Chad is measuring the size of different countries. He sees that Canada is 1.5 times bigger than the United States and Russia is 1/3 bigger than Canada. How many times bigger is Russia than the United States?"""
    size_US = 1
    size_CAN = 1.5 * size_US
    size_RUS = 1.33 * size_CAN
    times_bigger = size_RUS / size_US
    result = times_bigger
    return result

print(solution())