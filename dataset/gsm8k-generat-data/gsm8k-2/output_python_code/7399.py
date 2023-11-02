def solution():
    """Hana sold 4/7 of her stamp collection for $28. How much would she have earned from selling the entire collection?"""
    partial_sale_price = 28
    partial_sale_fraction = 4/7
    full_sale_price = partial_sale_price / partial_sale_fraction
    result = full_sale_price
    return result

print(solution())