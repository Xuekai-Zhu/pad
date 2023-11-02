def solution():
    koolaid_powder = 2  # Janice adds 2 tablespoons of koolaid powder
    initial_water = 16  # Janice adds 16 tablespoons of water
    evaporated_water = 4  # 4 tablespoons of water evaporate
    remaining_water = initial_water - evaporated_water  # Calculate the remaining water after evaporation
    new_water = remaining_water * 4  # Quadruple the amount of water in the jug
    total_liquid = koolaid_powder + new_water  # Calculate the total amount of liquid in the jug

    # Calculate the percentage of the liquid that is koolaid powder
    percent_koolaid = (koolaid_powder / total_liquid) * 100
    result = percent_koolaid
    return result

print(solution())