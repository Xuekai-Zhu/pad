def solution():
    """James has a rainwater collection barrel. For each inch of rain he collects 15 gallons. On Monday it rained 4 inches and on Tuesday it rained 3 inches. He can sell water for $1.2 per gallon. How much money did he make from selling all the water?"""
    # Define the gallons per inch of rain and the price per gallon
    GALLONS_PER_INCH = 15
    PRICE_PER_GALLON = 1.2

    # Calculate the total number of gallons collected
    total_gallons = (4 + 3) * GALLONS_PER_INCH

    # Calculate the total revenue from selling the water
    total_revenue = total_gallons * PRICE_PER_GALLON

    # Return the result
    result = total_revenue
    return result

print(solution())