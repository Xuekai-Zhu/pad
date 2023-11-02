def solution():
    """John's shirt cost 60% more than his pants. His pants cost $50. How much was John's outfit?"""
    # Define the cost of John's pants
    pants_cost = 50

    # Calculate the cost of John's shirt
    shirt_cost = pants_cost * 1.6

    # Calculate the total cost of John's outfit
    outfit_cost = pants_cost + shirt_cost

    result = outfit_cost
    return result

print(solution())