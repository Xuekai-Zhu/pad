def solution():
    
    total_pregnancies = 6 * 15
    total_babies = total_pregnancies * 4
    lost_babies = total_babies * 0.25
    expected_babies = total_babies - lost_babies
    result = expected_babies
    return result

print(solution())