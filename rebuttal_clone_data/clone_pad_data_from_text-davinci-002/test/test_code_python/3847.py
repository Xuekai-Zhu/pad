def solution():
    total_cups = 4 * 24
    damaged_cups = 5
    unused_cups = 30
    used_cups = total_cups - damaged_cups - unused_cups
    result = used_cups
    return result

print(solution())