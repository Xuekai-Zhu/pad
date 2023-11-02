def solution():
    x = 2 * original_number + 5
    x = 0.5 * original_number + 20
    original_number = (x - 20) / 1.5
    result = original_number
    return result

print(solution())