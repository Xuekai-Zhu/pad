def solution():
    total_land = 150
    house_and_machinery = 25
    future_expansion = 15
    cattle_land = 40

    # Calculate the total land used for non-crop purposes
    non_crop_land = house_and_machinery + future_expansion + cattle_land

    # Calculate the land used for crop production
    crop_land = total_land - non_crop_land
    result = crop_land
    return result

print(solution())