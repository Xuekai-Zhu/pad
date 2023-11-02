def solution():
    """John buys 1000 balloons. Each balloon holds 10 liters of air. If he buys 500-liter tanks of gas, how many tanks does he need to buy to fill all the balloons?"""
    total_liters = 1000 * 10
    tank_capacity = 500
    num_tanks = total_liters // tank_capacity
    if total_liters % tank_capacity != 0:
        num_tanks += 1
    result = num_tanks
    return result

print(solution())