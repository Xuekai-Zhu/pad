def solution():
    num_kettles = 6
    avg_pregnancies = 15
    num_babies_per_pregnancy = 4
    loss_percent = 0.25  # 25% loss

    # Calculate the total number of expected babies without loss
    total_babies = num_kettles * avg_pregnancies * num_babies_per_pregnancy

    # Calculate the number of lost babies
    lost_babies = total_babies * loss_percent

    # Calculate the final number of expected babies after loss
    expected_babies = total_babies - lost_babies
    result = expected_babies
    return result

print(solution())