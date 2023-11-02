def solution():
    
    raw_squat = 600
    sleeves_boost = 30
    wraps_boost = raw_squat * 0.25
    wraps_pounds = raw_squat + wraps_boost
    sleeves_pounds = raw_squat + sleeves_boost
    difference = wraps_pounds - sleeves_pounds
    result = difference
    return result

print(solution())