def solution():
    """A school bought pencils and pens. A pencil costs $2.50, while a pen costs $3.50. How much do 38 pencils and 56 pens cost?"""
    # Define the cost of each pencil and pen
    PENCIL_COST = 2.5
    PEN_COST = 3.5

    # Define the number of pencils and pens purchased
    num_pencils = 38
    num_pens = 56

    # Calculate the total cost of the pencils
    pencil_cost = num_pencils * PENCIL_COST

    # Calculate the total cost of the pens
    pen_cost = num_pens * PEN_COST

    # Calculate the total cost of all the items
    total_cost = pencil_cost + pen_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())