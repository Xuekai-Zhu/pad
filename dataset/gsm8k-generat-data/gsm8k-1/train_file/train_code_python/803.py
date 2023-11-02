def solution():
    """A zoo has 16 pandas, paired into mates (in the same zoo). Only 25% of the panda couples get pregnant after mating. If they each have one baby, how many panda babies are born?"""
    panda_pairs = 16
    pregnancy_rate = 0.25
    baby_rate = 1
    panda_babies = int(panda_pairs * pregnancy_rate * baby_rate)
    result = panda_babies
    return result

print(solution())