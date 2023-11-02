def solution():
    """In North Carolina, Jim bought 10 gallons of gas at $2.00/gallon. He paid $1.00 more per gallon in Virginia where he bought another 10 gallons of gas. How much has he spent on gas?"""
    # Define the cost per gallon in North Carolina and Virginia
    cost_nc = 2.0
    cost_va = 3.0

    # Calculate the total cost of gas purchased in North Carolina
    total_cost_nc = cost_nc * 10

    # Calculate the total cost of gas purchased in Virginia
    total_cost_va = cost_va * 10

    # Calculate the total amount spent on gas
    total_spent = total_cost_nc + total_cost_va

    # Return the result
    result = total_spent
    return result

print(solution())