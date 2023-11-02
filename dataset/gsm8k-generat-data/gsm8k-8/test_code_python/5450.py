def solution():
    # Calculate the total number of pregnancies
    total_pregnancies = 6 * 15

    # Calculate the total number of babies
    total_babies = total_pregnancies * 4

    # Calculate the number of lost babies
    lost_babies = total_babies * 0.25

    # Calculate the expected number of babies after accounting for lost babies
    expected_babies = total_babies - lost_babies
    result = expected_babies
    return result

print(solution())