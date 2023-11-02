def solution():
    total_ribbon = 4.5
    ribbon_per_box = 0.7
    leftover_ribbon = total_ribbon - (ribbon_per_box * total_ribbon)
    result = leftover_ribbon / ribbon_per_box
    return result

print(solution())