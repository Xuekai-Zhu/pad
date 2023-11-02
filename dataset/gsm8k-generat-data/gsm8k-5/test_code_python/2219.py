def solution():
    total_land = 150  # Job has 150 hectares of land in total
    house_and_machinery_land = 25  # Job's house and machinery occupy 25 hectares
    future_expansion_land = 15  # 15 hectares have been reserved for future expansion
    cattle_land = 40 # 40 hectares are dedicated to rearing cattle

    # Calculate the land used for crops
    crop_land = total_land - house_and_machinery_land - future_expansion_land - cattle_land
    result = crop_land
    return result

print(solution())