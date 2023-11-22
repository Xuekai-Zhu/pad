def solution():
    
    # Define the prices of the items
    milk_price = 2
    egg_price = 3
    light_bulb_price = 3
    cup_price = 3
    roach_trade_price = 4

    # Calculate the subtotal
    subtotal = milk_price + egg_price + light_bulb_price + cup_price + roach_trade_price

    # Calculate the tax
    tax = subtotal * 0.1

    # Calculate the total cost
    total_cost = subtotal + tax

    # Display the total cost
    result = total_cost
    return result

print(solution())