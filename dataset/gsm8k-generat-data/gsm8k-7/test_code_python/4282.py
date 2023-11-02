def solution():
    num_trees = 2 * 20         # total number of coconut trees
    num_coconuts = num_trees * 6   # total number of coconuts
    price_per_coconut = 0.50   # price of each coconut
    harvest_per_year = 4       # number of harvests per year
    harvest_per_6_months = 2   # number of harvests in 6 months

    # Calculate the total earnings from all coconuts harvested in 6 months
    total_earnings = num_coconuts * price_per_coconut * harvest_per_6_months

    result = total_earnings
    return result

print(solution())