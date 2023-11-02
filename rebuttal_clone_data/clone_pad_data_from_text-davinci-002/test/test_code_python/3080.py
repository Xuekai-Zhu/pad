def solution():
    kettles = 6
    average_pregnancies = 15
    babies_per_batch = 4
    percent_lost = 25
    expected_babies = kettles * average_pregnancies * babies_per_batch * ((100 - percent_lost) / 100)
    result = expected_babies
    return result

print(solution())