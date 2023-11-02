def solution():
    num_gifts = 8
    ribbon_per_gift = 1.5
    total_ribbon_needed = num_gifts * ribbon_per_gift
    ribbon_left = 15 - total_ribbon_needed
    result = ribbon_left
    return result

print(solution())