def solution():
    """Grandma wants to order 5 personalized backpacks for each of her grandchildren's first days of school.  The backpacks are 20% off of $20.00 and having their names monogrammed on the back pack will cost $12.00 each.  How much will the backpacks cost?"""
    # Define the original price and discount percentage
    ORIGINAL_PRICE = 20
    DISCOUNT_PERCENTAGE = 0.2

    # Calculate the discounted price of each backpack
    discounted_price = ORIGINAL_PRICE * (1 - DISCOUNT_PERCENTAGE)

    # Calculate the total cost of the backpacks before personalization
    total_cost_before_personalization = discounted_price * 5

    # Calculate the total cost of personalization
    personalization_cost = 12 * 5

    # Calculate the final total cost
    final_cost = total_cost_before_personalization + personalization_cost

    # Display the final total cost
    result = final_cost
    return result

print(solution())