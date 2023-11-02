def solution():
    """A bead shop sells one set of crystal beads at $9 each and one set of metal beads at $10 each. Nancy buys one set of crystal beads and two sets of metal beads. How much does she spend in all?"""
    # Define the price of crystal beads and metal beads
    crystal_price = 9
    metal_price = 10

    # Define the number of crystal beads and metal beads Nancy buys
    crystal_sets = 1
    metal_sets = 2

    # Calculate the total cost of Nancy's purchase
    total_cost = crystal_sets * crystal_price + metal_sets * metal_price

    result = total_cost
    return result

print(solution())