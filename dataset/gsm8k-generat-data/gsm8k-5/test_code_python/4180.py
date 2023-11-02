def solution():
    months_per_year = 12  # There are 12 months in a year
    months_per_bar = 2  # A bar of soap lasts for 2 months
    bars_per_year = months_per_year / months_per_bar  # Maria needs to buy this many bars of soap
    cost_per_bar = 8  # Each bar of soap costs $8.00

    # Calculate the total cost of buying enough soap for the entire year
    total_cost = bars_per_year * cost_per_bar
    result = total_cost
    return result

print(solution())