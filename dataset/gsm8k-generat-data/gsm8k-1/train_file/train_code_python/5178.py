def solution():
    """John has a large water collection tank. The tank can hold 200 gallons. It weighs 80 pounds empty. A rainstorm fills it to 80% of capacity. If a gallon of water weighs 8 pounds, how much does it weigh now?"""
    tank_capacity = 200
    empty_weight = 80
    filled_capacity = tank_capacity * 0.8
    filled_weight = filled_capacity * 8
    total_weight = empty_weight + filled_weight
    result = total_weight
    return result

print(solution())