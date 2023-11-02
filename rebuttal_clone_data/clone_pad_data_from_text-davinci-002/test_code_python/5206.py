def solution():
    control_plant = 36
    bone_meal_plant = 125
    cow_manure_plant = 200
    total_height = control_plant + (control_plant * (bone_meal_plant / 100)) +  (control_plant * (bone_meal_plant / 100) * (cow_manure_plant / 100))
    result = total_height
    return result

print(solution())