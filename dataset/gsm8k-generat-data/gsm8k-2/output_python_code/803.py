def solution():
    """A zoo has 16 pandas, paired into mates (in the same zoo). Only 25% of the panda couples get pregnant after mating. If they each have one baby, how many panda babies are born?"""
    panda_couples = 16 / 2
    pregnant_couples = panda_couples * 0.25
    panda_babies = pregnant_couples * 1
    result = panda_babies
    return result

print(solution())