def solution():
    # Calculate the total number of burgers needed
    burgers_needed = 3 * 9

    # Calculate the total number of buns needed
    buns_needed = burgers_needed + 8  # add one pack for the friend who doesn't eat bread

    # Calculate the number of packs of buns needed, rounding up to the nearest whole number
    packs_needed = math.ceil(buns_needed / 8)

    result = packs_needed
    return result

print(solution())