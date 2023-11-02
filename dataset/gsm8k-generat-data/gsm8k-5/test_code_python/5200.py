def solution():
    num_tshirts = 5  # Bryan bought 5 t-shirts
    price_tshirt = 100  # Each t-shirt costs $100
    total_cost = 1500  # Bryan spent $1500 in total
    cost_tshirts = num_tshirts * price_tshirt  # Calculate the cost of the t-shirts
    cost_pants = total_cost - cost_tshirts  # Subtract the cost of the t-shirts from the total cost to get the cost of the pants
    num_pants = 4  # Bryan bought 4 pairs of pants

    # Calculate the cost of each pair of pants
    cost_per_pant = cost_pants / num_pants
    result = cost_per_pant
    return result

print(solution())