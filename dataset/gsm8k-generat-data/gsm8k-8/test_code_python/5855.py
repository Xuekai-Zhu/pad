def solution():
    # work backwards to find the original number of gummy worms
    remaining_worms = 4
    for i in range(4):
        remaining_worms *= 2
        remaining_worms += 0.5 * remaining_worms
    original_worms = remaining_worms
    result = original_worms
    return result

print(solution())