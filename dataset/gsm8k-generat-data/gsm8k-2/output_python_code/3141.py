def solution():
    """Three-quarters of the oil from a 4000-liter tank (that was initially full) was poured into a 20000-liter capacity tanker that already had 3000 liters of oil. How many more liters of oil would be needed to make the large tanker half-full?"""
    initial_tank = 4000
    transferred_tank = initial_tank * 0.75
    total_oil = transferred_tank + 3000
    half_tanker = 20000 / 2
    additional_liters = half_tanker - total_oil
    result = additional_liters
    return result

print(solution())