def solution():
    panda_couples = 16
    percent_pregnant = 25
    pregnant_couples = panda_couples * (percent_pregnant / 100)
    babies_per_couple = 1
    total_babies = pregnant_couples * babies_per_couple
    result = total_babies
    return result

print(solution())