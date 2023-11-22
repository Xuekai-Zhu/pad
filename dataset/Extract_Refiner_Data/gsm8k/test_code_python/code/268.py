def solution():
    
    # Define the prices of the items
    cocoa_price = 4.20
    laundry_price = 9.45
    pasta_price = 1.35

    # Calculate the total cost of the items
    total_cost = cocoa_price + laundry_price + pasta_price

    # Calculate the amount of change the cashier gives back
    change = 20 - total_cost

    # return the result
    result = change
    return result

print(solution())