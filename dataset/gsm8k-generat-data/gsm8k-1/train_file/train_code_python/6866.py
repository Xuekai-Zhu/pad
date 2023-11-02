def solution():
    """Jack is a soccer player. He needs to buy two pairs of socks and a pair of soccer shoes. Each pair of socks cost $9.50, and the shoes cost $92. Jack has $40. How much more money does Jack need?"""
    num_socks = 2
    cost_per_pair_socks = 9.5
    cost_shoes = 92
    total_cost = (num_socks * cost_per_pair_socks) + cost_shoes
    money_available = 40
    money_needed = total_cost - money_available
    result = money_needed
    return result

print(solution())