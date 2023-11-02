def solution():
    # Calculate total land used for non-crop purposes
    non_crop_land = 25 + 15 + 40

    # Calculate crop land as the difference between total land and non-crop land
    crop_land = 150 - non_crop_land

    result = crop_land
    return result

print(solution())