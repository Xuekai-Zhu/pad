def solution():
    """Due to a drought, Jerry's household can only use 1000 gallons of water during July. Jerry uses 100 gallons for drinking and cooking and 20 gallons per shower. He wants to fill his pool, which measures 10 feet by 10 feet by 6 feet. If each gallon of water fills 1 cubic foot of the pool, how many showers can Jerry take in July?"""
    total_water_allowed = 1000
    water_used_for_drinking_and_cooking = 100
    water_used_for_pool = 10 * 10 * 6
    water_left_for_showers = total_water_allowed - water_used_for_drinking_and_cooking - water_used_for_pool
    showers_can_take = water_left_for_showers / 20
    result = showers_can_take
    return result

print(solution())