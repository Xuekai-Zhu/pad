def solution():
    """Mark constructs a cube of pure gold. The cube is 6 cm on each side. The density of gold is 19 grams per cubic centimeter. He buys the gold for $60 per gram. He sells it for 1.5 times its gold value. What was the profit? """
    # Define the size of the cube in cm
    cube_size = 6

    # Calculate the volume of the cube
    cube_volume = cube_size ** 3

    # Calculate the mass of the gold in the cube
    gold_mass = 19 * cube_volume

    # Calculate the cost of the gold
    gold_cost = 60 * gold_mass

    # Calculate the selling price of the gold
    gold_sell_price = 1.5 * gold_cost

    # Calculate the profit
    profit = gold_sell_price - gold_cost

    result = profit
    return result

print(solution())