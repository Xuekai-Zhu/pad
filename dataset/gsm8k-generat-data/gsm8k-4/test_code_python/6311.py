def solution():
    """An online website offers a flat rate shipping price of $5.00 if the purchase is below $50.00. If it's above $50.00 then they will charge 20% of the purchase price for shipping. Thomas orders 3 shirts for $12.00 each, a pack of socks for $5.00, 2 pairs of shorts for $15.00 each and a pair of swim trunks for $14.00 How much will his total bill be, including shipping?"""
    # Define the prices of each item
    shirt_price = 12.00
    socks_price = 5.00
    shorts_price = 15.00
    swim_trunks_price = 14.00

    # Calculate the total cost of the items
    total_cost = (shirt_price * 3) + socks_price + (shorts_price * 2) + swim_trunks_price

    # Determine the shipping cost based on the total cost
    if total_cost < 50:
        shipping_cost = 5.00
    else:
        shipping_cost = total_cost * 0.20

    # Calculate the final bill
    total_bill = total_cost + shipping_cost

    result = total_bill
    return result

print(solution())