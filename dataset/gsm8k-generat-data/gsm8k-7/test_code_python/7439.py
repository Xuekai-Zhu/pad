def solution():
    total_oranges = 96
    ripe_oranges = total_oranges / 2
    unripe_oranges = total_oranges / 2
    eaten_ripe_oranges = ripe_oranges / 4
    eaten_unripe_oranges = unripe_oranges / 8
    remaining_oranges = total_oranges - (eaten_ripe_oranges + eaten_unripe_oranges)
    result = remaining_oranges
    return result

print(solution())