def solution():
    """John has a raw squat of 600 pounds without sleeves or wraps. Sleeves add 30 pounds to his lift. Wraps add 25% to his squat. How much more pounds does he get out of wraps versus sleeves?"""
    raw_squat = 600
    sleeves_boost = 30
    wraps_boost = raw_squat * 0.25
    wraps_pounds = raw_squat + wraps_boost
    sleeves_pounds = raw_squat + sleeves_boost
    difference = wraps_pounds - sleeves_pounds
    result = difference
    return result

print(solution())