def solution():
    # Calculate the number of sheep Bob has
    bob_sheep = 300*2 + 35

    # Calculate the number of sheep Mary needs to have 69 fewer than Bob
    mary_sheep_needed = bob_sheep - 69 - 300

    # Calculate the number of sheep Mary needs to buy
    sheep_to_buy = mary_sheep_needed

    result = sheep_to_buy
    return result

print(solution())