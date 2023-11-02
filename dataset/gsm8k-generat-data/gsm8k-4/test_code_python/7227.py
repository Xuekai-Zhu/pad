def solution():
    """Elizabeth has 20 dollars and wants to buy pens and pencils. Each pencil costs $1.60 and each pen cost 2 dollars. How many pencils can she buy with her 20 dollars if she wants 6 pens?"""
    # Define the cost of a pencil and pen
    pencil_cost = 1.6
    pen_cost = 2

    # Define the number of pens Elizabeth wants to buy
    pens = 6

    # Calculate the total cost of the pens
    pens_cost = pens * pen_cost

    # Calculate the total amount Elizabeth has left after buying the pens
    remaining_amount = 20 - pens_cost

    # Calculate the maximum number of pencils Elizabeth can buy with the remaining amount
    pencils = remaining_amount // pencil_cost

    # Return the result
    result = int(pencils)
    return result

print(solution())