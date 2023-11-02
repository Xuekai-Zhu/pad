def solution():
    milk_per_glass = 6.5/8  # Each glass contains 6.5 ounces of milk out of 8 ounces
    syrup_per_glass = 1.5/8  # Each glass contains 1.5 ounces of chocolate syrup out of 8 ounces
    total_milk = 130  # Charles has 130 ounces of milk
    total_syrup = 60  # Charles has 60 ounces of chocolate syrup
    glasses = min(total_milk / milk_per_glass, total_syrup / syrup_per_glass)  # Charles can only make as many glasses as the ingredient that runs out first

    # Calculate the total ounces of chocolate milk Charles will drink
    total_ounces = glasses * 8  # Each glass is 8 ounces

    result = total_ounces
    return result

print(solution())