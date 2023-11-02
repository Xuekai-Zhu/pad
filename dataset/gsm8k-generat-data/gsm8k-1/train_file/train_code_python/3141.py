def solution():
    """Three-quarters of the oil from a 4000-liter tank (that was initially full) was poured into a 20000-liter capacity tanker that already had 3000 liters of oil. How many more liters of oil would be needed to make the large tanker half-full?"""
    initial_tank_capacity = 4000
    transfer_amount = initial_tank_capacity * 0.75
    initial_large_tank = 3000
    large_tank_capacity = 20000
    large_tank_level = initial_large_tank + transfer_amount
    half_tank_capacity = large_tank_capacity / 2
    liters_needed = half_tank_capacity - large_tank_level
    result = liters_needed
    return result

print(solution())