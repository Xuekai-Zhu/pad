def solution():
    """Mary has 300 sheep and Bob has double the number of sheep as Mary plus another 35. 
    How many sheep must Mary buy to have 69 fewer sheep than Bob?"""
    mary_sheep = 300
    bob_sheep = (2 * mary_sheep) + 35
    difference = bob_sheep - mary_sheep - 69
    mary_needs_to_buy = difference
    result = mary_needs_to_buy
    return result

print(solution())