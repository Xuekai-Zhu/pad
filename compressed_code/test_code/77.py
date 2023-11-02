def solution():
    
    gallons_per_inch = 15
    monday_inches = 4
    tuesday_inches = 3
    total_gallons = (monday_inches + tuesday_inches) * gallons_per_inch
    price_per_gallon = 1.2
    total_earnings = total_gallons * price_per_gallon
    result = total_earnings
    return result

print(solution())