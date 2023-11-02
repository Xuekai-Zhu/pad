def solution():
    
    total_gallons = 65
    cars_water = 2 * 7
    plant_water = cars_water - 11
    remaining_gallons = total_gallons - cars_water - plant_water
    plates_clothes_water = remaining_gallons / 2
    result = plates_clothes_water
    return result

print(solution())