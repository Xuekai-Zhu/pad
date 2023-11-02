def solution():
    """A third of the contestants at a singing competition are female, and the rest are male. If there are 18 contestants in total, how many of them are male?"""
    total_contestants = 18
    female_contestants = total_contestants / 3
    male_contestants = total_contestants - female_contestants
    result = male_contestants
    return result

print(solution())