def solution():
    """Mr. Caiden wants to do repairs to his house and requires 300 feet of metal roofing to do this. If each foot of roofing costs $8, and the supplier of the metal roofing brings in 250 feet of metal roofing for free, how much money is Mr. Caiden required to pay for the remaining metal roofing?"""
    # Define the required amount of metal roofing
    required_roofing = 300

    # Define the cost per foot of metal roofing
    cost_per_foot = 8

    # Calculate the total cost of the metal roofing
    total_cost = (required_roofing - 250) * cost_per_foot

    # Return the result
    result = total_cost
    return result

print(solution())