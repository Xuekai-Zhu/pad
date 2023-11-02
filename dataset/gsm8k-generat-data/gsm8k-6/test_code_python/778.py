def solution():
    # Calculate the total cost of the items that James bought
    total_cost = 3000

    # Subtract the cost of the TV and the bike that James returned
    total_cost -= (700 + 500)

    # Calculate the price at which James sold the bike
    price_bike_sold = 1.2 * 500 * 0.8

    # Subtract the price of the bike James sold and the price of the toaster
    total_cost -= (price_bike_sold + 100)

    result = total_cost
    return result

print(solution())