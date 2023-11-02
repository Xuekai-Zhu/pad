def solution():
    # Calculate the number of sheep that were rounded up
    sheep_rounded_up = 0.9 * 81

    # Calculate the number of sheep that wandered off
    sheep_wandered_off = 0.1 * 81

    # Calculate the total number of sheep
    total_sheep = sheep_rounded_up + sheep_wandered_off

    # Calculate the number of sheep out in the wilderness
    sheep_in_wilderness = sheep_wandered_off

    result = sheep_in_wilderness
    return result

print(solution())