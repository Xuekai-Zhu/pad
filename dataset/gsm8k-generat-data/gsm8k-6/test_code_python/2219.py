def solution():
    total_land = 150  # total land owned by Job in hectares
    occupied_land = 25 + 15 + 40  # hectares of land occupied by house, machinery and cattle rearing
    crop_land = total_land - occupied_land  # hectares of land used for crop production
    result = crop_land
    return result

print(solution())