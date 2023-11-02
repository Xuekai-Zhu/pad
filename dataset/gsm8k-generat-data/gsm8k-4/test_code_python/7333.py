def solution():
    """John buys a lightsaber toy. It is twice as expensive as all his other Star Wars toys combined. If his other Star Wars toys cost $1000, how much money has he spent in all after buying the lightsaber?"""
    # Define the cost of John's other Star Wars toys
    other_toys_cost = 1000

    # Calculate the cost of the lightsaber toy
    lightsaber_cost = 2 * other_toys_cost

    # Calculate the total cost of all the toys
    total_cost = other_toys_cost + lightsaber_cost

    result = total_cost
    return result

print(solution())