def solution():
    """A bushel of corn weighs 56 pounds and each individual ear of corn weighs .5 pounds. If Clyde picked 2 bushels of corn over the weekend, how many individual corn cobs did he pick?"""
    weight_per_bushel = 56
    weight_per_corn = 0.5
    total_weight = weight_per_bushel * 2
    total_corn = total_weight / weight_per_corn
    result = total_corn
    return result

print(solution())