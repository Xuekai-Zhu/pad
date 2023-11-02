def solution():
    """A performing magician has a disappearing act where he makes a random member of his audience disappear and reappear. Unfortunately, one-tenth of the time, the audience member never reappears. However, one-fifth of the time, two people reappear instead of only one. If the magician has put on 100 performances of the act this year, how many people have reappeared?"""
    total_disappearances = 100
    total_reappearances = 0

    for i in range(total_disappearances):
        # 10% of the time, person never reappears
        if random.randint(1, 10) == 1:
            continue
        # 20% of the time, two people reappear
        if random.randint(1, 5) == 1:
            total_reappearances += 2
        else:
            total_reappearances += 1

    result = total_reappearances
    return result

print(solution())