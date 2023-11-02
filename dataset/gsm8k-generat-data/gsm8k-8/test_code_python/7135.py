def solution():
    # Define the number of roses and how much each costs
    num_roses = 5 * 12
    cost_per_rose = 6

    # Calculate the total cost before discount
    total_cost = num_roses * cost_per_rose

    # Calculate the discounted price
    discounted_price = total_cost * 0.8
    result = discounted_price
    return result

print(solution())