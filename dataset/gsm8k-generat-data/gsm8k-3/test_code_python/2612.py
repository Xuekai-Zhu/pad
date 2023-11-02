def solution():
    """Janet buys 45-pound containers of cat litter for $21 each. If her cat litter box holds 15 pounds of cat litter, and she changes out the litter weekly, how much will it cost, in dollars, for her to buy enough litter to last 210 days?"""
    # Define the size and cost of each container of cat litter
    LITTER_SIZE = 45
    LITTER_COST = 21

    # Define the amount of litter Janet needs per week
    LITTER_PER_WEEK = 15

    # Calculate the number of containers of cat litter Janet will need for 210 days
    weeks = 210 / 7
    total_litter = weeks * LITTER_PER_WEEK
    containers = total_litter / LITTER_SIZE
    containers = math.ceil(containers) # Round up to the nearest whole container

    # Calculate the total cost of the cat litter
    total_cost = containers * LITTER_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())