def solution():
    """James has a rainwater collection barrel. For each inch of rain he collects 15 gallons. On Monday it rained 4 inches and on Tuesday it rained 3 inches. He can sell water for $1.2 per gallon. How much money did he make from selling all the water?"""
    gallons_per_inch = 15
    monday_rain = 4
    tuesday_rain = 3
    total_gallons_collected = (monday_rain + tuesday_rain) * gallons_per_inch
    price_per_gallon = 1.2
    total_money_made = total_gallons_collected * price_per_gallon
    result = total_money_made
    return result

print(solution())