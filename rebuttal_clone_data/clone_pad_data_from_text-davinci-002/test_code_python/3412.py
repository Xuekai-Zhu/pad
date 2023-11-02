def solution():
    ounces_of_milk = 130
    ounces_of_syrup = 60
    ounces_per_glass = 8
    milk_per_glass = 6.5
    syrup_per_glass = 1.5
    total_glasses = (ounces_of_milk / milk_per_glass) + (ounces_of_syrup / syrup_per_glass)
    total_ounces = total_glasses * ounces_per_glass
    result = total_ounces
    
    return result

print(solution())