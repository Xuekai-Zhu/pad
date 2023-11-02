def solution():
    """John's shirt cost 60% more than his pants.  His pants cost $50.  How much was John's outfit?"""
    # Define the cost of pants
    pants_cost = 50

    # Calculate the cost of the shirt
    shirt_cost = pants_cost * 1.6

    # Calculate the total cost of the outfit
    total_cost = pants_cost + shirt_cost

    # Display the total cost of the outfit
    result = total_cost
    return result

print(solution())