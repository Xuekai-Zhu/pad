def solution():
    # Calculate the total revenue from selling 10 pairs of sunglasses
    total_revenue = 30 * 10  # the vendor sells each pair for $30 and sells 10 pairs in a day

    # Calculate the total cost of the sunglasses and the new sign
    total_cost = total_revenue / 2 + 20  # the vendor uses half his profits to buy a new sign which costs $20

    # Calculate the cost of each pair of sunglasses
    cost_per_pair = total_cost / 10

    result = cost_per_pair
    return result

print(solution())