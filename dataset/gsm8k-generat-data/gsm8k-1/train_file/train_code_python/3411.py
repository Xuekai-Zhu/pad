def solution():
    """Charles is wondering how much chocolate milk he can make with all the supplies he finds in the fridge. He is going to keep drinking 8-ounce glasses until he uses up all the ingredients. Each glass must contain 6.5 ounces of milk and 1.5 ounces of chocolate syrup. If he has 130 ounces of milk and 60 ounces of chocolate syrup, how many total ounces ounce of chocolate milk will he drink?"""
    milk_per_glass = 6.5
    syrup_per_glass = 1.5
    total_milk = 130
    total_syrup = 60
    glasses = min(total_milk/milk_per_glass, total_syrup/syrup_per_glass)
    total_chocolate_milk = glasses * 8
    result = total_chocolate_milk
    return result

print(solution())