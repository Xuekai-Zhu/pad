def solution():
    abaddon_location = "below the earth"
    ahura_mazda_location = "high above the sky"
    # Check if Ahura Mazda is located above Abaddon
    if ahura_mazda_location > abaddon_location:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())