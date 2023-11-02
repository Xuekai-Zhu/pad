def solution():
    # Calculate the total cost of James' purchases
    total_cost = 3000

    # Calculate the amount of the returned TV and bike
    returned_cost = 700 + 500

    # Calculate the amount received for selling the bike
    sold_cost = 0.8 * 1.2 * 500

    # Calculate the total cost after returns and sale
    total_cost = total_cost - returned_cost + sold_cost - 100

    # Calculate the out of pocket amount
    out_of_pocket = total_cost - 3000
    result = out_of_pocket
    return result

print(solution())