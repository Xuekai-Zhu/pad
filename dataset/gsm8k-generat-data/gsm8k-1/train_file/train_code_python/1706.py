def solution():
    """Anais has 30 more toys than Kamari. There are 160 toys altogether. How many toys are there in Kamari's box?"""
    total_toys = 160
    difference = 30
    # Let x be the number of toys Kamari has
    # Then, Anais has x+30 toys
    # And, x+(x+30) = 160 (total toys)
    # Simplifying, 2x+30 = 160
    # Solving for x, x = 65
    kamari_toys = (total_toys - difference) / 2
    result = kamari_toys
    return result

print(solution())