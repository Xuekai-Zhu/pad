def solution():
    """A bushel of corn weighs 56 pounds and each individual ear of corn weighs .5 pounds. If Clyde picked 2 bushels of corn over the weekend, how many individual corn cobs did he pick?"""
    corn_per_bushel = 56 / 0.5
    bushels_picked = 2
    total_corn = corn_per_bushel * bushels_picked
    result = total_corn
    return result

print(solution())