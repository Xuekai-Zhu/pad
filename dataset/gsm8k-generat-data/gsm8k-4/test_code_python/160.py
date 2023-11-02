def solution():
    """John throws a block party and splits the cost with 3 other people. They buy 100 pounds of burgers at $3 per pound. They also buy $80 of condiments and propane to cook everything. John also buys all the alcohol which costs $200. How much did John spend altogether"""
    # Define the cost of the burgers and the additional costs
    burger_cost = 100 * 3
    additional_costs = 80 + 200

    # Calculate the total cost of the party
    total_cost = burger_cost + additional_costs

    # Divide the total cost by 4 to find John's share
    john_share = total_cost/4

    # Return the result
    result = john_share
    return result

print(solution())