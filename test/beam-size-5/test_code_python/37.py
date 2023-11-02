def solution():
    # Calculate the distance outside of the dragon's flames
    distance_outside_flames = 1000 - 400 - (3 * 400)  # Polly could throw the javelin three times farther than when not holding the gemstone
    result = distance_outside_flames
    return result

print(solution())