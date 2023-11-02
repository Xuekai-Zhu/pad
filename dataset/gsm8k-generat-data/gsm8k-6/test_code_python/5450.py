def solution():
    # Calculate the total number of babies expected
    total_pregnancies = 6 * 15  # 6 kettles, each with an average of 15 pregnancies
    total_babies = total_pregnancies * 4  # each pregnancy yields 4 babies
    lost_babies = total_babies * 0.25  # 25% of babies may be lost
    expected_babies = total_babies - lost_babies
    result = expected_babies
    return result

print(solution())