def solution():
    
    gallons_per_inch = 15
    monday_rain = 4
    tuesday_rain = 3
    total_gallons_collected = (monday_rain + tuesday_rain) * gallons_per_inch
    price_per_gallon = 1.2
    total_money_made = total_gallons_collected * price_per_gallon
    result = total_money_made
    return result

print(solution())