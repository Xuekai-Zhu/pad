def solution():
    tree_length = 80  # John cuts down an 80-foot tree
    logs_per_foot = 4  # John cuts the tree into 4-foot logs
    total_logs = tree_length * logs_per_foot  # John can make logs out of 80% of the tree
    planks_cut = 5  # John cuts the logs into 5 planks
    price_per_plank = 1.2  # John sells each plank for $1.2

    # Calculate the total number of planks John can make
    total_planks = total_logs / planks_cut

    # Calculate the total revenue from selling the logs
    total_revenue = total_planks * price_per_plank
    result = total_revenue
    return result

print(solution())