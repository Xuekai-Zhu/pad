def solution():
    # Calculate the number of fleas the dog had before the treatments
    fleas_before = 14 * 2 ** 4  # each treatment gets rid of half the fleas, and there were 4 treatments
    fleas_after = 14  # given in the problem statement
    more_fleas_before = fleas_before - fleas_after
    result = more_fleas_before
    return result

print(solution())