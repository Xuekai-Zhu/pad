def solution():
    """John has a large water collection tank. The tank can hold 200 gallons. It weighs 80 pounds empty. A rainstorm fills it to 80% of capacity. If a gallon of water weighs 8 pounds, how much does it weigh now?"""
    tank_capacity = 200
    empty_tank_weight = 80
    filled_tank_volume = 0.8 * tank_capacity
    filled_tank_weight = (filled_tank_volume * 8) + empty_tank_weight
    result = filled_tank_weight
    return result

print(solution())