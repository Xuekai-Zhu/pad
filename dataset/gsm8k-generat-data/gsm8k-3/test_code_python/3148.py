def solution():
    """Mr. Zubir bought a pair of pants, a shirt, and a coat. The pair of pants and shirt costs $100. The pants and coat cost $244. The coat costs 5 times as much as the shirt. How much did Mr. Zubir pay for his coat?"""
    # Define the cost of the pair of pants and shirt
    pants_shirt_cost = 100

    # Define the cost of the pants and coat
    pants_coat_cost = 244

    # Calculate the cost of the coat
    # Let x be the cost of the shirt
    # Then, according to the problem, the cost of the coat is 5x
    # We can write two equations based on the given information:
    # x + 5x = pants_coat_cost - pants_shirt_cost
    # 6x = 144
    # x = 24
    shirt_cost = 24
    coat_cost = 5 * shirt_cost

    # Display the cost of the coat
    result = coat_cost
    return result

print(solution())