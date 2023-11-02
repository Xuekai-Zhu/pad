def solution():
    """A watermelon stand sold 46 watermelons. Seventeen customers bought one melon, three customers bought three melons, and the rest bought two melons. How many customers bought two watermelons?"""
    # Define the total number of watermelons sold and the number of customers who bought only one watermelon
    total_watermelons = 46
    one_watermelon_customers = 17

    # Calculate the number of watermelons bought by customers who bought 3 melons
    three_watermelons = 3 * 3

    # Calculate the number of watermelons bought by customers who bought 2 melons
    two_watermelons = total_watermelons - one_watermelon_customers - three_watermelons

    # Calculate the number of customers who bought 2 melons
    two_watermelon_customers = two_watermelons // 2

    # Return the result
    result = two_watermelon_customers
    return result

print(solution())