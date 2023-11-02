def solution():
    """Jack went to a supermarket with $100 and bought 4 bottles of water. Then his mother called him and asked him to buy twice as many bottles as he already bought. Each bottle cost $2. Finally, he also bought half a pound of cheese and 1 pound of cheese costs $10. How much money does Jack have remaining?"""
    # Define the initial amount of money Jack had
    initial_money = 100

    # Calculate the cost of the first 4 bottles of water
    water_cost = 4 * 1.5
    remaining_money = initial_money - water_cost

    # Calculate the cost of the additional bottles of water
    additional_water_cost = 2 * 2 * 1.5
    remaining_money -= additional_water_cost

    # Calculate the cost of the cheese
    cheese_cost = 10 * 0.5
    remaining_money -= cheese_cost

    # Return the remaining amount of money
    result = remaining_money
    return result

print(solution())