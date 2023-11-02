def solution():
    
    total_land = 150
    house_and_machinery = 25
    future_expansion = 15
    cattle_land = 40
    crop_land = total_land - house_and_machinery - future_expansion - cattle_land
    result = crop_land
    return result

print(solution())