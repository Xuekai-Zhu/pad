def solution():
    num_socks_pairs = 2
    socks_price = 9.5
    shoes_price = 92
    total_money = 40

    # Calculate the total cost of all socks
    total_socks_cost = num_socks_pairs * socks_price

    # Calculate the total cost of the shoes
    total_shoes_cost = shoes_price

    # Calculate the total cost of all items
    total_cost = total_socks_cost + total_shoes_cost

    # Calculate the difference between the total cost and the amount of money Jack has
    difference = total_cost - total_money
    result = difference
    return result

print(solution())