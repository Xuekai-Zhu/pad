def solution():
    """Janice adds 2 tablespoons of koolaid power and 16 tablespoons of water to a jug. She leaves it out long enough for 4 tablespoons of water to evaporate. Then she quadruples the amount of water in the jug. What percentage of the liquid in the jug is koolaid powder?"""
    koolaid_power = 2
    initial_water = 16
    evaporated_water = 4
    remaining_water = initial_water - evaporated_water
    total_water = remaining_water * 4
    total_liquid = total_water + koolaid_power
    percentage_koolaid = (koolaid_power / total_liquid) * 100
    result = percentage_koolaid
    return result

print(solution())