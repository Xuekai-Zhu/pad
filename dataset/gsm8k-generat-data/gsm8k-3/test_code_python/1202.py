def solution():
    """A man is trying to decide between two apartments based on monthly costs, including utilities and driving-related costs. The first apartment costs $800/month in rent and $260/month in utilities, and is further from work (31 miles/day). The second apartment costs $900/month in rent and $200/month in utilities, and is closer to work (21 miles/day). Each mile driven costs 58 cents. If the man must drive to work 20 days per month, what is the difference between the total monthly costs of these two apartments?"""
    
    # Define costs for each apartment
    rent1 = 800
    rent2 = 900
    utils1 = 260
    utils2 = 200
    miles1 = 31 * 20
    miles2 = 21 * 20
    mile_cost = 0.58
    
    # Calculate the total costs for each apartment
    total_cost1 = rent1 + utils1 + miles1 * mile_cost
    total_cost2 = rent2 + utils2 + miles2 * mile_cost
    
    # Calculate the difference in costs between the two apartments
    cost_difference = round(total_cost2 - total_cost1)
    
    # Return the result
    return cost_difference

print(solution())