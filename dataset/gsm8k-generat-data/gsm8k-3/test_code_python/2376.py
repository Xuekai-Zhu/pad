def solution():
    """A local restaurant was offering a "Build Your Own Hot Brownie" dessert.  The brownie cost $2.50 and each scoop of ice cream costs $1.00.  Any syrup costs $0.50 and nuts cost $1.50.  If Juanita orders the brownie with 2 scoops of ice cream, double syrup, and nuts, how much will her dessert cost?"""
    # Define the cost of each component
    BROWNIE_COST = 2.5
    ICE_CREAM_COST = 1
    SYRUP_COST = 0.5
    NUTS_COST = 1.5

    # Define the number of each component Juanita orders
    ice_cream_scoops = 2
    syrup_amount = 2
    nuts_amount = 1

    # Calculate the total cost of Juanita's dessert
    total_cost = BROWNIE_COST + (ICE_CREAM_COST * ice_cream_scoops) + (SYRUP_COST * syrup_amount * 2) + (NUTS_COST * nuts_amount)

    # Display the total cost
    result = total_cost
    return result

print(solution())