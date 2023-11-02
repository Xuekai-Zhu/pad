def solution():
    # Define the number of pants and the original price
    num_pants = 10
    original_price = 45

    # Calculate the discounted price and total cost before tax
    discounted_price = original_price * 0.8
    total_cost_before_tax = num_pants * discounted_price

    # Calculate the cost after tax
    cost_after_tax = total_cost_before_tax * 1.1

    result = cost_after_tax
    return result

print(solution())