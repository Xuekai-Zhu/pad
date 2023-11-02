def solution():
    """Frank went to a shop to buy some food for his breakfast. He bought 10 buns for $0.1 each, two bottles of milk, for $2 each, and a carton of eggs, which was three times more expensive than one bottle of milk. How much did Frank pay for his breakfast shopping?"""
    bun_price = 0.1
    milk_price = 2
    carton_price = 3 * milk_price
    bun_total = 10 * bun_price
    milk_total = 2 * milk_price
    carton_total = carton_price
    total_cost = bun_total + milk_total + carton_total
    result = total_cost
    return result

print(solution())