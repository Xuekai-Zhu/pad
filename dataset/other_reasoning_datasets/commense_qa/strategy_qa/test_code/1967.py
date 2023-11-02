def solution():
    gray_whale_length = 39
    pool_diameter_range = range(10, 34)
    if gray_whale_length < max(pool_diameter_range):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())