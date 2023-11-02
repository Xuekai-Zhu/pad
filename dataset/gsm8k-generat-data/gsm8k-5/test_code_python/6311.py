def solution():
    shirt_price = 12  # Each shirt costs $12
    num_shirts = 3  # Thomas orders 3 shirts
    sock_price = 5  # The pack of socks costs $5
    short_price = 15  # Each pair of shorts costs $15
    num_shorts = 2  # Thomas orders 2 pairs of shorts
    swim_trunks_price = 14  # The swim trunks cost $14

    # Calculate the total cost of the order
    subtotal = (shirt_price * num_shirts) + sock_price + (short_price * num_shorts) + swim_trunks_price

    # Calculate the shipping cost
    if subtotal < 50:
        shipping_cost = 5  # Flat rate shipping cost for orders under $50
    else:
        shipping_cost = 0.2 * subtotal  # 20% shipping cost for orders over $50

    # Calculate the total bill, including shipping
    total_bill = subtotal + shipping_cost
    result = total_bill
    return result

print(solution())