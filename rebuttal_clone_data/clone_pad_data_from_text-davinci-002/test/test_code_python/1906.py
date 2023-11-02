def solution():
    us_size = 1
    canada_size = 1.5
    russia_size = canada_size + (canada_size / 3)
    result = russia_size / us_size
    return result

print(solution())