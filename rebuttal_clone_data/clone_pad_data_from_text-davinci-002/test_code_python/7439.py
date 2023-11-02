def solution():
    oranges = 96
    ripe_oranges = oranges / 2
    eaten_ripe_oranges = ripe_oranges / 4
    unripe_oranges = oranges / 2
    eaten_unripe_oranges = unripe_oranges / 8
    eaten_oranges = eaten_ripe_oranges + eaten_unripe_oranges
    result = eaten_oranges
    
    return result

print(solution())