def solution():
    # Calculate the total amount of water collected in gallons
    water_collected = 4 * 15 + 3 * 15  # 15 gallons of water for each inch of rain collected
    # Calculate the total amount of money made from selling the water
    money_made = water_collected * 1.2  # $1.2 per gallon of water sold
    result = money_made
    return result

print(solution())