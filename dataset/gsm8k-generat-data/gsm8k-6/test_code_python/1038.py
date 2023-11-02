def solution():
    total_seeds = 23
    uneaten_seeds = total_seeds - 5  # five seeds never grew into plants
    grown_plants = uneaten_seeds / 3  # a third of the remaining seeds grew
    eaten_plants = grown_plants / 3  # a third of the uneaten plants were strangled by weeds

    # Marge pulled 2 weeds, so only (grown_plants - eaten_plants - 2) plants remained
    remaining_plants = grown_plants - eaten_plants - 2
    result = remaining_plants + 1  # add one for the weed Marge let grow
    return result

print(solution())