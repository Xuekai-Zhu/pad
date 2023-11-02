def solution():
    """An aquarium holds an equal number of clownfish and blowfish. 26 of the blowfish stay in their own tank, and the remaining blowfish swim into a display tank. An equal number of clownfish join the blowfish in the display tank, but then a third of these clownfish swim back into their own tank. If the aquarium holds a combined total of 100 fish, how many clownfish are now in the display tank?"""
    total_fish = 100
    blowfish_tank_one = 26
    blowfish_tank_two = total_fish - blowfish_tank_one
    clownfish_tank_one = blowfish_tank_two
    clownfish_tank_two = clownfish_tank_one - (clownfish_tank_one / 3)
    result = clownfish_tank_two
    return result

print(solution())