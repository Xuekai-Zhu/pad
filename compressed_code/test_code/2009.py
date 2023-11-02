def solution():
    
    cost_per_gallon = 3.5
    glasses_per_gallon = 16
    total_gallons = 2
    total_glasses = total_gallons * glasses_per_gallon
    cost_of_lemonade = total_gallons * cost_per_gallon
    sold_glasses = total_glasses - 5 - 6
    revenue = sold_glasses * 1
    profit = revenue - cost_of_lemonade
    result = profit
    return result

print(solution())