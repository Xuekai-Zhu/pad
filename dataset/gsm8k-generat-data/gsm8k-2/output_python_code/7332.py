def solution():
    """John buys a lightsaber toy. It is twice as expensive as all his other Star Wars toys combined. If his other Star Wars toys cost $1000, how much money has he spent in all after buying the lightsaber?"""
    other_toys_cost = 1000
    lightsaber_cost = 2 * other_toys_cost
    total_cost = other_toys_cost + lightsaber_cost
    result = total_cost
    return result

print(solution())