def solution():
    """Darryl is an inventor who just designed a new machine. He had to pay $3600 for the parts to construct the machine, and $4500 for the patent he applied for once he built it. If the machine sells for $180, how many machines does Darryl need to sell to break even after the costs?"""
    # Define the costs and selling price per machine
    parts_cost = 3600
    patent_cost = 4500
    selling_price = 180

    # Calculate the total cost per machine
    total_cost = parts_cost + patent_cost

    # Calculate the number of machines needed to break even
    break_even_quantity = total_cost / (selling_price - total_cost)

    # Round off the result
    result = round(break_even_quantity)
    return result

print(solution())