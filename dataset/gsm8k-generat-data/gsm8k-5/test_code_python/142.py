def solution():
    # Percentage of germs killed by the first spray
    spray_1 = 50

    # Percentage of germs killed by the second spray
    spray_2 = 25

    # Percentage of germs killed by both sprays (taking into account the overlapping 5%)
    both_sprays = spray_1 + (spray_2 - (spray_1 * spray_2 / 100))

    # Percentage of germs left after using both sprays together
    germs_left = 100 - both_sprays
    result = germs_left
    return result

print(solution())