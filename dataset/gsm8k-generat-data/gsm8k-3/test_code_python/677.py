def solution():
    """Mr. Caiden wants to do repairs to his house and requires 300 feet of metal roofing to do this. If each foot of roofing costs $8, and the supplier of the metal roofing brings in 250 feet of metal roofing for free, how much money is Mr. Caiden required to pay for the remaining metal roofing?"""
    # Define the cost per foot of metal roofing
    COST_PER_FOOT = 8

    # Define the required amount of metal roofing and the amount received for free
    required_feet = 300
    free_feet = 250

    # Calculate the amount of metal roofing that Mr. Caiden needs to pay for
    remaining_feet = required_feet - free_feet

    # Calculate the total cost of the remaining metal roofing
    remaining_cost = remaining_feet * COST_PER_FOOT

    # Display the cost of the remaining metal roofing
    result = remaining_cost
    return result

print(solution())