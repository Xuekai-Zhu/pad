def solution():
    # Define the cost of one mani/pedi
    regular_cost = 40.00

    # Calculate the discount amount
    discount = 0.25 * regular_cost

    # Calculate the discounted cost of one mani/pedi
    discounted_cost = regular_cost - discount

    # Calculate the total cost for 5 mani/pedis
    total_cost = 5 * discounted_cost
    result = total_cost
    return result

print(solution())