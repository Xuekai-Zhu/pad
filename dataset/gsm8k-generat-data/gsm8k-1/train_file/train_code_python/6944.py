def solution():
    """Josh buys 3 packs of string cheese. Each piece of string cheese cost 10 cents. Each pack has 20 string cheeses in them. How many dollars did he pay?"""
    packs_of_cheese = 3
    cost_per_cheese = 0.1
    cheeses_per_pack = 20
    total_cheeses = packs_of_cheese * cheeses_per_pack
    total_cost = total_cheeses * cost_per_cheese
    result = total_cost
    return result

print(solution())