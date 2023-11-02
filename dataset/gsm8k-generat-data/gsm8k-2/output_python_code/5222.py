def solution():
    """Spongebob works in a burger shop. If he sells 30 burgers for $2 each and 12 large fries for $1.5. How much will Spongebob earn for the day?"""
    burger_count = 30
    burger_price = 2
    fries_count = 12
    fries_price = 1.5
    total_burger_sales = burger_count * burger_price
    total_fries_sales = fries_count * fries_price
    total_sales = total_burger_sales + total_fries_sales
    result = total_sales
    return result

print(solution())