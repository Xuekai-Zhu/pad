def solution():
    """Mark constructs a cube of pure gold. The cube is 6 cm on each side. The density of gold is 19 grams per cubic centimeter. He buys the gold for $60 per gram. He sells it for 1.5 times its gold value. What was the profit?"""
    side_length = 6
    volume = side_length ** 3
    density = 19
    mass = volume * density
    gold_value = mass * 60
    sale_price = gold_value * 1.5
    profit = sale_price - (gold_value)
    result = profit
    return result

print(solution())