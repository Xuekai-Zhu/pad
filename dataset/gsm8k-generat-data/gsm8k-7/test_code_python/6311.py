def solution():
    shirt_price = 12.0
    num_shirts = 3

    socks_price = 5.0

    shorts_price = 15.0
    num_shorts = 2

    swim_trunks_price = 14.0

    # Calculate the total cost of all items
    total_cost = (shirt_price * num_shirts) + socks_price + (shorts_price * num_shorts) + swim_trunks_price

    # Check if the total cost is above $50
    if total_cost > 50:
        shipping_cost = total_cost * 0.2
    else:
        shipping_cost = 5.0

    # Calculate the total bill including shipping
    total_bill = total_cost + shipping_cost
    result = total_bill
    return result

print(solution())