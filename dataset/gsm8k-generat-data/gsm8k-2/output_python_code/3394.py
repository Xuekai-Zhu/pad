def solution():
    """Chad is measuring the size of different countries. He sees that Canada is 1.5 times bigger than the United States and Russia is 1/3 bigger than Canada. How many times bigger is Russia than the United States?"""
    us_size = 1
    canada_size = 1.5 * us_size
    russia_size = (1 + (1/3)) * canada_size
    russia_to_us_ratio = russia_size / us_size
    result = russia_to_us_ratio
    return result

print(solution())