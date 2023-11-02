def solution():
    """A watermelon stand sold 46 watermelons. Seventeen customers bought one melon, three customers bought three melons, and the rest bought two melons. How many customers bought two watermelons?"""
    # Define the number of watermelons sold and the number of customers who bought one and three melons
    total_watermelons = 46
    one_melon_customers = 17
    three_melon_customers = 3

    # Calculate the number of watermelons bought by customers who bought one and three melons
    one_melon_count = one_melon_customers * 1
    three_melon_count = three_melon_customers * 3

    # Calculate the total number of watermelons bought by customers who did not buy one or three melons
    other_watermelons = total_watermelons - one_melon_count - three_melon_count

    # Calculate the number of customers who bought two melons
    two_melon_customers = other_watermelons // 2

    # Display the number of customers who bought two melons
    result = two_melon_customers
    return result

print(solution())