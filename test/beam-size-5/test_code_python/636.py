def solution():
    base_price = 30000  # The base price of the truck is $30,000
    extra_price = 7500  # The extra price of the king cab upgrade is $7,500
    leather_seat_price = base_price / 3  # The leather seats are one-third the cost of the king cab upgrade
    running_boards_price = leather_seat_price - 500  # The running boards are $500 less than the leather seats

    # Calculate the total cost of the two-ton truck
    total_cost = base_price + extra_price + leather_seat_price + running_boards_price
    result = total_cost
    return result

print(solution())