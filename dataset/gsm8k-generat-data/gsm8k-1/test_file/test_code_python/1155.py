def solution():
    """Carla just gave birth to identical octuplets. She dresses 3/4 of them in purple and 1/4 in blue. If all the blue-wearers and 1/3 of the purple wearers also wear bows, what is the percentage chance a baby wearing a bow is wearing purple?"""
    total_babies = 8
    purple_babies = total_babies * (3/4)
    blue_babies = total_babies - purple_babies
    purple_with_bows = purple_babies * (1/3)
    blue_with_bows = blue_babies
    bow_wearers = purple_with_bows + blue_with_bows
    purple_bow_wearers = purple_with_bows
    probability = (purple_bow_wearers / bow_wearers) * 100
    result = probability
    return result

print(solution())