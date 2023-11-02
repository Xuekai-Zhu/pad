def solution():
    """Penny has $20. Penny buys 4 pairs of socks for $2 a pair and a hat for $7. How much money does Penny have left?"""
    # Define the initial amount of money
    initial_money = 20

    # Define the cost of socks and hat
    sock_price = 2
    hat_price = 7

    # Define the number of socks and hat that Penny buys
    socks_bought = 4
    hat_bought = 1

    # Calculate the total cost
    total_cost = (socks_bought * sock_price) + (hat_bought * hat_price)

    # Calculate the remaining money
    remaining_money = initial_money - total_cost

    # return the result
    result = remaining_money
    return result

print(solution())