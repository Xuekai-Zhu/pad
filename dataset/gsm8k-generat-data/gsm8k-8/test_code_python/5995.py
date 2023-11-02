def solution():
    # Mary's number of sheep
    mary_sheep = 300
    # Bob's number of sheep
    bob_sheep = (2 * mary_sheep) + 35
    # Calculate how many sheep Mary needs to buy
    mary_buy_sheep = (bob_sheep - 69) - mary_sheep
    result = mary_buy_sheep
    return result

print(solution())