def solution():
    """Penny has $20. Penny buys 4 pairs of socks for $2 a pair and a hat for $7. How much money does Penny have left?"""
    # Define the initial amount of money Penny has
    initial_money = 20

    # Define the cost of each item
    socks_cost = 2
    hat_cost = 7

    # Define the number of items purchased
    num_socks = 4
    num_hats = 1

    # Calculate the total cost of the items purchased
    total_cost = (socks_cost * num_socks) + (hat_cost * num_hats)

    # Calculate the amount of money Penny has left
    money_left = initial_money - total_cost

    # Display the amount of money Penny has left
    result = money_left
    return result

print(solution())