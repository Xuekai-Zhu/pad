def solution():
    
    price_per_gallon = 3.00
    cashback_per_gallon = 0.20
    gallons_bought = 10
    total_price = price_per_gallon * gallons_bought
    total_revenue = total_price * cashback_per_gallon
    final_price = total_revenue - total_price
    result = final_price
    return result

print(solution())