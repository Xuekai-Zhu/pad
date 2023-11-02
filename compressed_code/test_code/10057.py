def solution():
    
    num_kettles = 6
    num_pregnancies = 15
    num_babies_per_pregnancy = 4
    total_babies = num_kettles * num_pregnancies * num_babies_per_pregnancy
    lost_babies = 0.25 * total_babies
    expected_babies = total_babies - lost_babies
    result = expected_babies
    return result

print(solution())