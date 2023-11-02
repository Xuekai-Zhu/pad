def solution():
    """A box of six popsicles was left out in the sun and is slowly melting. Every time a popsicle melts the remaining popsicles melt twice as fast as the previous one. How many times faster than the first popsicle does the last popsicle’s remains melt?"""
    popsicles = 6
    melting_rate = [1] * popsicles

    for i in range(popsicles):
        for j in range(i):
            melting_rate[j] *= 2
        melting_rate[i] *= 2

    result = melting_rate[-1] / melting_rate[0]
    return result

print(solution())