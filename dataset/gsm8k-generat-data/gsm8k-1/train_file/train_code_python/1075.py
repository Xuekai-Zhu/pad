def solution():
    """Stella’s antique shop has 3 dolls, 2 clocks and 5 glasses for sale. She sells the dolls for $5 each. The clocks are priced at $15 each.
    The glasses are priced at $4 each. If she spent $40 to buy everything and she sells all of her merchandise, how much profit will she make?"""
    dolls = 3
    clocks = 2
    glasses = 5
    doll_price = 5
    clock_price = 15
    glass_price = 4
    total_cost = 40
    total_profit = (dolls * doll_price) + (clocks * clock_price) + (glasses * glass_price) - total_cost
    result = total_profit
    return result

print(solution())