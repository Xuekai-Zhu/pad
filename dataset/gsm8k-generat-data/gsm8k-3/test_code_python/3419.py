def solution():
    """ Luis needed to buy some socks. He bought 4 pairs of red socks and 6 pairs of blue ones. In total, he spent $42. If the red socks cost $3 each, how much did he pay for each blue pair? """

    # Define the cost of a red sock
    RED_SOCK_PRICE = 3

    # Define the number of pairs of each color of socks
    RED_PAIRS = 4
    BLUE_PAIRS = 6

    # Calculate the total cost of the red socks
    red_cost = RED_PAIRS * RED_SOCK_PRICE * 2

    # Calculate the total cost of all the socks
    total_cost = 42

    # Calculate the cost of each blue pair
    blue_cost = (total_cost - red_cost) / BLUE_PAIRS

    # Display the cost of each blue pair
    result = blue_cost
    return result

print(solution())