def solution():
    gallons_per_inch = 15
    selling_price_per_gallon = 1.2

    monday_rain_inches = 4
    tuesday_rain_inches = 3

    # Calculate the total number of gallons collected from both days of rain
    total_gallons_collected = (monday_rain_inches + tuesday_rain_inches) * gallons_per_inch

    # Calculate the total revenue from selling all the water
    total_revenue = total_gallons_collected * selling_price_per_gallon
    result = total_revenue
    return result

print(solution())