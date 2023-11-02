def solution():
    """Axel bought an aquarium that was marked down 50% from an original price of $120. But he also paid additional sales tax equal to 5% of the reduced price. What was the total cost of the aquarium?"""
    # Calculate the reduced price of the aquarium
    reduced_price = 120 * 0.5

    # Calculate the amount of sales tax
    sales_tax = reduced_price * 0.05

    # Calculate the total cost of the aquarium
    total_cost = reduced_price + sales_tax

    # Display the total cost
    result = total_cost
    return result

print(solution())