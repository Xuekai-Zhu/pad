def solution():
    """Anais has 30 more toys than Kamari. There are 160 toys altogether. How many toys are there in Kamari's box?"""
    total_toys = 160
    anais_toys = (total_toys + 30) / 2
    kamari_toys = total_toys - anais_toys
    result = kamari_toys
    return result

print(solution())