def solution():
    """The first store charges $3 for 6 apples while the second store charges $4 for 10 apples. How many cents can you save on each apple from buying $4 for 10 apples than from $3 for 6 apples?"""
    first_store_price = 3
    first_store_quantity = 6
    second_store_price = 4
    second_store_quantity = 10
    first_store_unit_price = first_store_price / first_store_quantity
    second_store_unit_price = second_store_price / second_store_quantity
    cents_saved_per_apple = (first_store_unit_price - second_store_unit_price) * 100
    result = cents_saved_per_apple
    return result

print(solution())