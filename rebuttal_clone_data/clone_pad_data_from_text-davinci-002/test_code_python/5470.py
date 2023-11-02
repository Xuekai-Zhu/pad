def solution():
    total_picked_up = 17 + 52
    spiral_broken = 52 / 2
    not_spiral_perfect = 12
    spiral_perfect = 17 - not_spiral_perfect
    result = spiral_broken - spiral_perfect
    return result

print(solution())