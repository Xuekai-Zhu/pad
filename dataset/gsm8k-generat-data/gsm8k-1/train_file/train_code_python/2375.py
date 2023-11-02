def solution():
    """A local restaurant was offering a "Build Your Own Hot Brownie" dessert. The brownie cost $2.50 and each scoop of ice cream costs $1.00. Any syrup costs $0.50 and nuts cost $1.50. If Juanita orders the brownie with 2 scoops of ice cream, double syrup, and nuts, how much will her dessert cost?"""
    brownie_cost = 2.5
    ice_cream_cost = 1.0
    syrup_cost = 0.5
    nuts_cost = 1.5
    
    num_ice_cream_scoops = 2
    num_syrup = 2
    num_nuts = 1
    
    total_cost = brownie_cost + (num_ice_cream_scoops * ice_cream_cost) + (num_syrup * syrup_cost) + (num_nuts * nuts_cost)
    result = total_cost
    return result

print(solution())