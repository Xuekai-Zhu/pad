def solution():
    """Stella's antique shop has 3 dolls, 2 clocks and 5 glasses for sale. She sells the dolls for $5 each. The clocks are priced at $15 each. The glasses are priced at $4 each. If she spent $40 to buy everything and she sells all of her merchandise, how much profit will she make?"""
  
    doll_price = 5
    clock_price = 15
    glass_price = 4
    dolls = 3
    clocks = 2
    glasses = 5
    total_spent = 40
    total_profit = (doll_price * dolls) + (clock_price * clocks) + (glass_price * glasses) - total_spent
    result = total_profit
    return result

print(solution())