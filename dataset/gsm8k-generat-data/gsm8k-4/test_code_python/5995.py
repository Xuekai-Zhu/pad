def solution():
    """Mary has 300 sheep and Bob has double the number of sheep as Mary plus another 35. How many sheep must Mary buy to have 69 fewer sheep than Bob?"""
    # Define the initial number of sheep
    mary_sheep = 300

    # Calculate the number of sheep Bob has
    bob_sheep = mary_sheep * 2 + 35

    # Calculate the number of sheep Mary needs to buy to have 69 fewer than Bob
    mary_buy = bob_sheep - mary_sheep - 69

    # return the result
    result = mary_buy
    return result

print(solution())