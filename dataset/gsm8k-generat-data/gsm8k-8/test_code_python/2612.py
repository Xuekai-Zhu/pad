def solution():
    # Calculate the amount of cat litter Janet needs for 210 days
    total_cat_litter_needed = 210 / 7 * 15

    # Calculate the number of 45-pound containers she needs to buy
    num_containers_needed = total_cat_litter_needed / 45

    # Calculate the total cost of the cat litter
    total_cost = num_containers_needed * 21

    result = total_cost
    return result

print(solution())