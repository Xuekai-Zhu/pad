def solution():
    # Calculate the number of sheep that wandered off into the hills
    sheep_in_pen = 81
    sheep_rounded_up = 0.9 * sheep_in_pen
    sheep_wandered_off = sheep_in_pen - sheep_rounded_up
    result = sheep_wandered_off
    return result

print(solution())