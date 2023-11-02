def solution():
    """A bear is preparing to hibernate for the winter and needs to gain 1000 pounds. At the end of summer, the bear feasts on berries and small woodland animals. During autumn, it devours acorns and salmon. It gained a fifth of the weight it needed from berries during summer, and during autumn, it gained twice that amount from acorns. Salmon made up half of the remaining weight it had needed to gain. How many pounds did it gain eating small animals?"""
    total_weight = 1000
    berries_weight = total_weight * 0.2
    acorns_weight = total_weight * 0.4
    salmon_weight = total_weight * 0.5
    small_animal_weight = total_weight - (berries_weight + acorns_weight + salmon_weight)
    result = small_animal_weight
    return result

print(solution())