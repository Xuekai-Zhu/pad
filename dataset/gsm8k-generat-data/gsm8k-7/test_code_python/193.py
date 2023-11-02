def solution():
    height_A = 192
    increase = 0.2  # 20% increase
    height_B = height_A / (1 + increase)
    result = height_B
    return result

print(solution())