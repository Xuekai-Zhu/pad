def solution():
    sweets_total = 27
    sweets_kept = 27 / 3
    sweets_eldest = 8
    sweets_youngest = sweets_eldest / 2
    sweets_second = (sweets_total - sweets_kept) - (sweets_eldest + sweets_youngest)
    result = sweets_second
    return result

print(solution())