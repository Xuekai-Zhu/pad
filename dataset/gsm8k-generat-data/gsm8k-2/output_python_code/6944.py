def solution():
    """Josh buys 3 packs of string cheese. Each piece of string cheese cost 10 cents. Each pack has 20 string cheeses in them. How many dollars did he pay?"""
    packs = 3
    cheese_per_pack = 20
    price_per_cheese = 0.1
    total_cheeses = packs * cheese_per_pack
    total_price = total_cheeses * price_per_cheese
    dollars_paid = total_price / 100
    result = dollars_paid
    return result

print(solution())