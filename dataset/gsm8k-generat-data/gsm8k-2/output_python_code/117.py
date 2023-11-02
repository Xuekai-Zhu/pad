def solution():
    """An aquarium holds an equal number of clownfish and blowfish. 26 of the blowfish stay in their own tank, and the remaining blowfish swim into a display tank.
    An equal number of clownfish join the blowfish in the display tank, but then a third of these clownfish swim back into their own tank.
    If the aquarium holds a combined total of 100 fish, how many clownfish are now in the display tank?"""
    total_fish = 100
    blowfish_stay = 26
    display_blowfish = (total_fish - blowfish_stay)/2
    display_clownfish = display_blowfish
    clownfish_return = display_clownfish/3
    display_clownfish -= clownfish_return
    result = display_clownfish
    return result

print(solution())