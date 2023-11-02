def solution():
    num_subs = 2
    subs_price = 7.5

    num_chips = 2
    chips_price = 1.5

    num_cookies = 2
    cookies_price = 1.0

    delivery_fee = 0.2  # 20% delivery fee added
    tip = 5.0

    # Calculate the total cost of all subs
    total_subs_cost = num_subs * subs_price

    # Calculate the total cost of all chips
    total_chips_cost = num_chips * chips_price

    # Calculate the total cost of all cookies
    total_cookies_cost = num_cookies * cookies_price

    # Calculate the total cost of all delivery
    total_delivery_cost = total_subs_cost + total_chips_cost + total_cookies_cost

    # Calculate the delivery fee
    delivery_fee = total_delivery_cost * delivery_fee

    # Add the delivery fee to the tip
    total_delivery_cost += tip

    result = total_delivery_cost
    return

print(solution())