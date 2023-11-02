def solution():
    
    milk_per_glass = 6.5
    syrup_per_glass = 1.5
    total_milk = 130
    total_syrup = 60
    glasses = min(total_milk/milk_per_glass, total_syrup/syrup_per_glass)
    total_chocolate_milk = glasses * 8
    result = total_chocolate_milk
    return result

print(solution())