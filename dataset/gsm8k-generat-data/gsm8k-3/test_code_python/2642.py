def solution():
    """George had $100. He bought a shirt for $24 and he also bought a pair of socks. Then he had $65 left. How much is a pair of socks?"""
    # Define the initial amount of money George had
    initial_amount = 100

    # Define the cost of the shirt
    shirt_cost = 24

    # Define the amount of money George had left after buying the shirt
    amount_left = 65

    # Calculate the amount of money George spent on the shirt and socks
    spent_money = initial_amount - amount_left

    # Calculate the cost of the socks
    sock_cost = spent_money - shirt_cost

    # Display the cost of the socks
    result = sock_cost
    return result

print(solution())