def solution():
    """Mr. Finnegan has 3 tanks with a capacity of 7000 gallons, 5000 gallons, and 3000 gallons, respectively.
    If he fills the first tank up to 3/4 full, the second tank with water up to 4/5 of its capacity,
    and the third tank up to half of its capacity, how many gallons in total are in the tanks?"""
    tank_1_capacity = 7000
    tank_1_amount = 0.75 * tank_1_capacity

    tank_2_capacity = 5000
    tank_2_amount = 0.8 * tank_2_capacity

    tank_3_capacity = 3000
    tank_3_amount = 0.5 * tank_3_capacity

    total_amount = tank_1_amount + tank_2_amount + tank_3_amount
    result = total_amount
    return result

print(solution())