def solution():
    
    milk_price = 3
    milk_discount = 1
    cereal_discount = 1
    milk_savings_per_gallon = milk_price - 2
    cereal_savings_per_box = cereal_discount
    total_milk_savings = milk_savings_per_gallon * 3
    total_cereal_savings = cereal_savings_per_box * 5
    total_savings = total_milk_savings + total_cereal_savings
    result = total_savings
    return result

print(solution())