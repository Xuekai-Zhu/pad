def solution():
    asking_price = 5200  # Chris is selling his car for $5200

    # Offer 1: buyer pays full price if Chris pays for maintenance inspection
    inspection_cost = asking_price / 10  # Cost of maintenance inspection is 1/10 of asking price
    offer1_price = asking_price + inspection_cost  # Total price for offer 1
    offer1_profit = asking_price - inspection_cost  # Profit for offer 1

    # Offer 2: buyer pays full price if Chris replaces headlights ($80) and tires (3 times the cost of headlights)
    headlights_cost = 80
    tires_cost = 3 * headlights_cost
    offer2_price = asking_price + headlights_cost + tires_cost  # Total price for offer 2
    offer2_profit = asking_price - (headlights_cost + tires_cost)  # Profit for offer 2

    # Calculate the difference between the profits from the two offers
    profit_difference = offer1_profit - offer2_profit
    result = profit_difference
    return result

print(solution())