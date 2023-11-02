def solution():
    # Calculate the total square footage of Mancino's gardens
    mancino_garden_sqft = 3 * (16*5)  # 3 gardens, each measuring 16 ft by 5 ft
    # Calculate the total square footage of Marquita's gardens
    marquita_garden_sqft = 2 * (8*4)  # 2 gardens, each measuring 8 ft by 4 ft
    # Calculate the combined square footage of all gardens
    total_sqft = mancino_garden_sqft + marquita_garden_sqft
    result = total_sqft
    return result

print(solution())