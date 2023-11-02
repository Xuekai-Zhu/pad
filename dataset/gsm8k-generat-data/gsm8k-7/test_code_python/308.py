def solution():
    charcoal_per_ml = 2/30  # 2 grams of charcoal per 30 ml of water
    water = 900  # 900 ml of water

    # Calculate the total charcoal needed based on the amount of water used
    charcoal_needed = charcoal_per_ml * water

    result = charcoal_needed
    return result

print(solution())