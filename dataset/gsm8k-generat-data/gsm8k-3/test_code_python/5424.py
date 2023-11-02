def solution():
    """A bead shop sells one set of crystal beads at $9 each and one set of metal beads at $10 each. Nancy buys one set of crystal beads and two sets of metal beads. How much does she spend in all?"""
    # Define the price of crystal beads and metal beads
    CRYSTAL_PRICE = 9
    METAL_PRICE = 10

    # Define the number of sets of crystal beads and metal beads purchased by Nancy
    crystal_sets = 1
    metal_sets = 2

    # Calculate the total cost of crystal beads and metal beads purchased by Nancy
    crystal_cost = crystal_sets * CRYSTAL_PRICE
    metal_cost = metal_sets * METAL_PRICE

    # Calculate the total cost of all the beads purchased by Nancy
    total_cost = crystal_cost + metal_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())