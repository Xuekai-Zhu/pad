def solution():
    """Mark constructs a cube of pure gold. The cube is 6 cm on each side. The density of gold is 19 grams per cubic centimeter. He buys the gold for $60 per gram. He sells it for 1.5 times its gold value. What was the profit?"""
    cube_volume = 6 ** 3
    gold_density = 19
    gold_weight = cube_volume * gold_density
    gold_price = 60
    total_cost = gold_weight * gold_price
    selling_price = 1.5 * total_cost
    profit = selling_price - total_cost
    result = profit
    return result

print(solution())