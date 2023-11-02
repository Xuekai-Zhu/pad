def solution():
    """Axel bought an aquarium that was marked down 50% from an original price of $120. But he also paid additional sales tax equal to 5% of the reduced price. What was the total cost of the aquarium?"""
    # Define the original price of the aquarium
    original_price = 120

    # Calculate the price after the 50% discount
    discounted_price = original_price * 0.5

    # Calculate the additional cost due to the sales tax
    tax_cost = discounted_price * 0.05

    # Calculate the total cost of the aquarium
    total_cost = discounted_price + tax_cost

    # return the result
    result = total_cost
    return result

print(solution())