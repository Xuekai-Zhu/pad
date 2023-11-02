def solution():
    """A watermelon stand sold 46 watermelons. Seventeen customers bought one melon, three customers bought three melons, and the rest bought two melons. How many customers bought two watermelons?"""
    total_customers = 46
    one_melon_customers = 17
    three_melon_customers = 3
    two_melon_customers = total_customers - one_melon_customers - three_melon_customers
    result = two_melon_customers
    return result

print(solution())