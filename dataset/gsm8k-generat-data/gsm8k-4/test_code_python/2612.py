def solution():
    """Janet buys 45-pound containers of cat litter for $21 each. If her cat litter box holds 15 pounds of cat litter, and she changes out the litter weekly, how much will it cost, in dollars, for her to buy enough litter to last 210 days?"""
    # Define the size of the cat litter box
    litter_box_size = 15

    # Calculate the amount of litter needed for 210 days
    total_litter_needed = litter_box_size * 7 * 30

    # Calculate the number of containers needed
    containers_needed = total_litter_needed / 45

    # Calculate the total cost of the cat litter
    total_cost = containers_needed * 21

    result = total_cost
    return result

print(solution())