def solution():
    """A dog is being treated for fleas. One flea treatment gets rid of half the fleas. After four treatments, the dog has 14 fleas left. How many more fleas did the dog have before the flea treatments than after?"""
    fleas_after_treatment = 14
    flea_reduction = 0.5
    total_fleas = fleas_after_treatment / flea_reduction
    fleas_before_treatment = total_fleas - fleas_after_treatment
    result = fleas_before_treatment
    return result

print(solution())