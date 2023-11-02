def solution():
    fleas_left = 14  # After four treatments, the dog has 14 fleas left
    fleas_before_treatment = fleas_left * 2 ** 4  # Each treatment gets rid of half the fleas, so four treatments get rid of (1/2)^4 = 1/16 of the fleas

    # Calculate the difference in fleas before and after treatment
    diff = fleas_before_treatment - fleas_left
    result = diff
    return result

print(solution())