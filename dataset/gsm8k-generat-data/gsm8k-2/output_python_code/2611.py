def solution():
    """Janet buys 45-pound containers of cat litter for $21 each. If her cat litter box holds 15 pounds of cat litter, and she changes out the litter weekly, how much will it cost, in dollars, for her to buy enough litter to last 210 days?"""
    total_litter_needed = 210/7 * 15  # Calculate total amount of litter needed in pounds
    num_containers = total_litter_needed / 45  # Calculate number of 45-pound containers needed
    total_cost = num_containers * 21  # Calculate total cost
    result = total_cost
    return result

print(solution())