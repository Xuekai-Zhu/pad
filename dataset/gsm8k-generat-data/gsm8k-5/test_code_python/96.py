def solution():
    gallons_collected_monday = 4 * 15  # James collected 15 gallons for each inch of rain on Monday
    gallons_collected_tuesday = 3 * 15  # James collected 15 gallons for each inch of rain on Tuesday
    total_gallons_collected = gallons_collected_monday + gallons_collected_tuesday  # Total gallons collected
    sale_price = 1.2  # James can sell each gallon of water for $1.2

    # Calculate the total amount of money James made from selling water
    total_money_made = total_gallons_collected * sale_price
    result = total_money_made
    return result

print(solution())