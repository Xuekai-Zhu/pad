def solution():
    total_roses = 10 * 20
    red_roses = total_roses / 2
    white_roses = 3 * (total_roses / 5)
    pink_roses = total_roses - red_roses - white_roses
    result = pink_roses
    return result

print(solution())