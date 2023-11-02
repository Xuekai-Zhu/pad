def solution():
    distance = 2800   # miles
    shout_distance = 100   # meters
    # Convert distance to meters for comparison
    distance = distance * 1609.34
    if distance <= shout_distance:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())