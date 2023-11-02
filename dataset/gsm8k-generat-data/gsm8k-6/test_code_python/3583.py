def solution():
    # Let x be the amount of fertilizer in gallons
    x = 60 / 4  # Total amount of seed and fertilizer is 60 gallons and 1 square meter needs 1/4 gallons of seed and fertilizer combined
    seed = 3 * x  # Each square meter needs three times as much seed as fertilizer

    result = seed
    return result

print(solution())