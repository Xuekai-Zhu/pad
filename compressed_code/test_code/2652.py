def solution():
    
    milk_per_glass = 6.5
    syrup_per_glass = 1.5
    total_milk = 130
    total_syrup = 60

    num_glasses = min(total_milk/milk_per_glass, total_syrup/syrup_per_glass)
    total_choc_milk = num_glasses * 8
    
    result = total_choc_milk
    return result

print(solution())