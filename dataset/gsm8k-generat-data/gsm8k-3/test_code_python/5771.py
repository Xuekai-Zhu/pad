def solution():
    """James buys 10 shirts and half as many pants.  The shirts cost $6 each and the pants cost $8 each.  How much did everything cost?"""
    # Define the number of shirts James buys
    num_shirts = 10

    # Calculate the number of pants James buys
    num_pants = num_shirts / 2

    # Calculate the cost of all the shirts
    shirt_cost = num_shirts * 6

    # Calculate the cost of all the pants
    pant_cost = num_pants * 8

    # Calculate the total cost of everything
    total_cost = shirt_cost + pant_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())