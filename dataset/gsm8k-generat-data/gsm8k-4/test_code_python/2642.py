def solution():
    """George had $100. He bought a shirt for $24 and he also bought a pair of socks. Then he had $65 left. How much is a pair of socks?"""
    # Define the initial amount of money George had and the cost of the shirt
    initial_money = 100
    shirt_cost = 24

    # Calculate the amount of money left after buying the shirt
    money_left = initial_money - shirt_cost

    # Calculate the cost of the socks
    socks_cost = money_left - 65

    # return the result
    result = socks_cost
    return result

print(solution())