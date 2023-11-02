def solution():
    """Jamal bought 4 half dozen colored crayons at $2 per crayon. What was the total cost of the crayons that she bought?"""
    # Define the number of crayons per half dozen
    CRAYONS_PER_HALF_DOZEN = 6

    # Define the cost per crayon
    COST_PER_CRAYON = 2

    # Define the number of half dozens purchased
    half_dozens = 4

    # Calculate the total number of crayons purchased
    total_crayons = half_dozens * CRAYONS_PER_HALF_DOZEN

    # Calculate the total cost of the crayons purchased
    total_cost = total_crayons * COST_PER_CRAYON

    # return the result
    result = total_cost
    return result

print(solution())