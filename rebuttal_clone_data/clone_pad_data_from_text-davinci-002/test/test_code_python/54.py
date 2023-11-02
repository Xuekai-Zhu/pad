def solution():
    
    inches_of_rain_on_monday = 4
    inches_of_rain_on_tuesday = 3
    total_inches_of_rain = inches_of_rain_on_monday + inches_of_rain_on_tuesday
    gallons_collected = total_inches_of_rain * 15
    price_per_gallon = 1.2
    total_revenue = gallons_collected * price_per_gallon
    result = total_revenue
    return result

print(solution())