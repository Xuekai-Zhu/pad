def solution():
    """Darryl is an inventor who just designed a new machine. He had to pay $3600 for the parts to construct the machine, and $4500 for the patent he applied for once he built it. If the machine sells for $180, how many machines does Darryl need to sell to break even after the costs?"""
    # Define the cost of parts and patent fees
    PARTS_COST = 3600
    PATENT_COST = 4500

    # Define the selling price of the machine
    SELLING_PRICE = 180

    # Calculate the total cost to build and patent the machine
    total_cost = PARTS_COST + PATENT_COST

    # Calculate the number of machines Darryl needs to sell to break even
    break_even_quantity = total_cost / (SELLING_PRICE - PARTS_COST)

    # Display the number of machines Darryl needs to sell to break even
    result = break_even_quantity
    return result

print(solution())