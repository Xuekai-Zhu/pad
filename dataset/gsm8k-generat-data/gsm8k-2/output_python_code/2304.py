def solution():
    """A 40 meters rope was cut into 2 parts in the ratio of 2:3. How long is the shorter part?"""
    total_length = 40
    ratio = 2/3
    shorter_part = total_length * (ratio/(1+ratio))
    result = shorter_part
    return result

print(solution())