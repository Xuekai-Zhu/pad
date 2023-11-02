def solution():
    koolaid_powder = 2
    water_original = 16
    water_evaporated = 4

    # Calculate the remaining water after evaporation
    water_remaining = water_original - water_evaporated

    # Quadruple the amount of water in the jug
    water_new = water_remaining * 4

    # Calculate the total volume of liquid in the jug
    total_liquid = koolaid_powder + water_new

    # Calculate the percentage of the liquid that is koolaid powder
    percent_koolaid = (koolaid_powder / total_liquid) * 100
    result = percent_koolaid
    return result

print(solution())