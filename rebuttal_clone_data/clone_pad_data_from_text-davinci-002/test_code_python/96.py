def solution():
    """James has a rainwater collection barrel. For each inch of rain he collects 15 gallons. On Monday it rained 4 inches and on Tuesday it rained 3 inches. He can sell water for $1.2 per gallon. How much money did he make from selling all the water?"""
    inches_of_rain_on_monday = 4
    inches_of_rain_on_tuesday = 3
    total_inches_of_rain = inches_of_rain_on_monday + inches_of_rain_on_tuesday
    gallons_collected = total_inches_of_rain * 15
    price_per_gallon = 1.2
    total_revenue = gallons_collected * price_per_gallon
    result = total_revenue
    return result

print(solution())