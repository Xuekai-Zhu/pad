def solution():
    num_kettles = 6  # There are 6 kettles being tracked
    avg_pregnancies = 15  # Each kettle has an average of 15 pregnancies
    babies_per_batch = 4  # Each pregnancy yields 4 babies
    lost_pct = 0.25  # Approximately 25% of babies are lost

    # Calculate the total number of babies expected without lost babies
    total_babies = num_kettles * avg_pregnancies * babies_per_batch

    # Calculate the number of lost babies
    lost_babies = total_babies * lost_pct

    # Calculate the expected number of babies after accounting for lost babies
    expected_babies = total_babies - lost_babies
    result = expected_babies
    return result

print(solution())