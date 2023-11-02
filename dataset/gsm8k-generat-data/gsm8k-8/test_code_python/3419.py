def solution():
    # Define the number of red and blue socks and their respective costs
    red_socks = 4
    blue_socks = 6
    red_cost = 3

    # Calculate the total cost of red socks
    total_red_cost = red_socks * red_cost

    # Calculate the total cost of socks, and then the cost of blue socks
    total_cost = 42
    blue_cost = (total_cost - total_red_cost) / blue_socks
    result = blue_cost
    return result

print(solution())