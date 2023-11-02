def solution():
    """A watermelon stand sold 46 watermelons. Seventeen customers bought one melon, three customers bought three melons, and the rest bought two melons. How many customers bought two watermelons?"""
    total_melons = 46
    one_melon_customers = 17
    three_melons_customers = 3
    two_melons_customers = total_melons - one_melon_customers - three_melons_customers
    result = two_melons_customers
    return result

print(solution())