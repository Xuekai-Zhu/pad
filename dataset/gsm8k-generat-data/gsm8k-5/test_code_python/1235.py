def solution():
    starting_amount = 20  # Penny starts with $20
    socks_cost = 2  # A pair of socks costs $2
    hat_cost = 7  # A hat costs $7

    # Calculate the total cost of Penny's purchases
    total_cost = (4 * socks_cost) + hat_cost

    # Calculate how much money Penny has left after her purchases
    money_left = starting_amount - total_cost
    result = money_left
    return result

print(solution())