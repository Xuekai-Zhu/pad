def solution():
    """Martha has 18 crayons. She lost half of them, so she bought a new set of 20 crayons. How many crayons in total does Martha have after the purchase?"""
    initial_crayons = 18
    lost_crayons = initial_crayons / 2
    new_crayons = 20
    total_crayons = initial_crayons - lost_crayons + new_crayons
    result = total_crayons
    return result

print(solution())