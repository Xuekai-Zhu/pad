def solution():
    """Mary has 300 sheep and Bob has double the number of sheep as Mary plus another 35. How many sheep must Mary buy to have 69 fewer sheep than Bob?"""
    mary_sheep = 300
    bob_sheep = (mary_sheep * 2) + 35
    new_mary = bob_sheep - 69 - mary_sheep
    result = new_mary
    return result

print(solution())