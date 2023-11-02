def solution():
    # Calculate the maximum number of chocolate milk glasses that Charles can make
    max_glasses = min(130/6.5, 60/1.5)  # using the ratio of milk to chocolate syrup
    total_ounces = max_glasses * 8  # since each glass contains 8 ounces
    result = total_ounces
    return result

print(solution())