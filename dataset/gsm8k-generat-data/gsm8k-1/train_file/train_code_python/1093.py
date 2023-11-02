def solution():
    """Janice adds 2 tablespoons of koolaid power and 16 tablespoons of water to a jug. She leaves it out long enough for 4 tablespoons of water to evaporate. Then she quadruples the amount of water in the jug. What percentage of the liquid in the jug is koolaid powder?"""
    koolaid_powder = 2
    initial_water = 16
    evaporation = 4
    remaining_water = initial_water - evaporation
    total_liquid = remaining_water + koolaid_powder
    quadrupled_water = 4 * remaining_water
    percentage_koolaid = (koolaid_powder / total_liquid) * 100
    result = percentage_koolaid
    return result

print(solution())