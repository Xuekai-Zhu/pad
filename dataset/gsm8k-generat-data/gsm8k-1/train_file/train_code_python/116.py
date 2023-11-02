def solution():
    """An aquarium holds an equal number of clownfish and blowfish. 26 of the blowfish stay in their own tank, and the remaining blowfish swim into a display tank. An equal number of clownfish join the blowfish in the display tank, but then a third of these clownfish swim back into their own tank. If the aquarium holds a combined total of 100 fish, how many clownfish are now in the display tank?"""
    total_fish = 100
    blowfish_stay = 26
    blowfish_display = total_fish / 2 - blowfish_stay
    clownfish_display = blowfish_display / 2
    clownfish_return = clownfish_display / 3
    clownfish_final = clownfish_display - clownfish_return
    result = clownfish_final
    return result

print(solution())