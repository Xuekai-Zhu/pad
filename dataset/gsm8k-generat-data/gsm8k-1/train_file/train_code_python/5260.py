def solution():
    """Due to a drought, Jerry's household can only use 1000 gallons of water during July. Jerry uses 100 gallons for drinking and cooking and 20 gallons per shower. He wants to fill his pool, which measures 10 feet by 10 feet by 6 feet. If each gallon of water fills 1 cubic foot of the pool, how many showers can Jerry take in July?"""
    total_water_allowance = 1000
    water_used_for_drinking_cooking = 100
    water_used_for_pool = 10 * 10 * 6
    water_remaining = total_water_allowance - water_used_for_drinking_cooking - water_used_for_pool
    water_per_shower = 20
    showers_possible = water_remaining / water_per_shower
    result = int(showers_possible)
    return result

print(solution())