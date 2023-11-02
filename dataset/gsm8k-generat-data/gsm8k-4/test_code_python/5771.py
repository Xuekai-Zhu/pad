def solution():
    """James buys 10 shirts and half as many pants. The shirts cost $6 each and the pants cost $8 each. How much did everything cost?"""
    # Define the number of shirts and pants
    num_shirts = 10
    num_pants = num_shirts // 2

    # Calculate the total cost of the shirts
    shirt_cost = num_shirts * 6

    # Calculate the total cost of the pants
    pant_cost = num_pants * 8

    # Calculate the total cost of everything
    total_cost = shirt_cost + pant_cost

    # return the result
    result = total_cost
    return result

print(solution())