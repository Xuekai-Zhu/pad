def solution():
    """George had $100. He bought a shirt for $24 and he also bought a pair of socks. Then he had $65 left. How much is a pair of socks?"""
    initial_money = 100
    shirt_cost = 24
    remaining_money = 65
    socks_cost = (initial_money - shirt_cost - remaining_money)
    result = socks_cost
    return result

print(solution())