def solution():
    
    # Define the prices of the items
    hamburger_price = 4
    fries_price = 0.3
    fruit_drink_price = 2

    # Calculate the total cost of the items
    total_cost = (5 * hamburger_price) + (10 * fries_price) + (5 * fruit_drink_price)

    # Calculate the amount of change Carly will get back
    change = 50 - total_cost

    # return the result
    result = change
    return result

print(solution())