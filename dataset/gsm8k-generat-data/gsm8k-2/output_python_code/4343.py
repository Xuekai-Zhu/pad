def solution():
    """Allie has 9 toys, which are in total worth $52. If we know that one toy is worth $12, and all the other toys have the same value, how much does one of the other toys cost?"""
    total_value = 52
    known_value = 12
    unknown_value = (total_value - known_value) / 8
    result = unknown_value
    return result

print(solution())