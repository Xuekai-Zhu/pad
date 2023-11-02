def solution():
    """An online website offers a flat rate shipping price of $5.00 if the purchase is below $50.00.  If it's above $50.00 then they will charge 20% of the purchase price for shipping.  Thomas orders 3 shirts for $12.00 each, a pack of socks for $5.00, 2 pairs of shorts for $15.00 each and a pair of swim trunks for $14.00  How much will his total bill be, including shipping?"""
    # Define the prices of each item
    SHIRT_PRICE = 12
    SOCKS_PRICE = 5
    SHORTS_PRICE = 15
    TRUNKS_PRICE = 14

    # Define the number of each item Thomas ordered
    shirt_count = 3
    sock_count = 1
    shorts_count = 2
    trunks_count = 1

    # Calculate the subtotal
    subtotal = (shirt_count * SHIRT_PRICE) + (sock_count * SOCKS_PRICE) + (shorts_count * SHORTS_PRICE) + (trunks_count * TRUNKS_PRICE)

    # Determine the shipping cost
    if subtotal < 50:
        shipping_cost = 5
    else:
        shipping_cost = subtotal * 0.2

    # Calculate the total bill
    total_bill = subtotal + shipping_cost

    # Display the total bill
    result = total_bill
    return result

print(solution())