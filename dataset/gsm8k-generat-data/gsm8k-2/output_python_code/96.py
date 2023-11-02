def solution():
    """James has a rainwater collection barrel. For each inch of rain he collects 15 gallons. On Monday it rained 4 inches and on Tuesday it rained 3 inches. He can sell water for $1.2 per gallon. How much money did he make from selling all the water?"""
    gallons_per_inch = 15
    monday_inches = 4
    tuesday_inches = 3
    total_gallons = (monday_inches + tuesday_inches) * gallons_per_inch
    price_per_gallon = 1.2
    total_earnings = total_gallons * price_per_gallon
    result = total_earnings
    return result

print(solution())