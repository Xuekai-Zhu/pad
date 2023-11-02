def solution():
    """The first store charges $3 for 6 apples while the second store charges $4 for 10 apples. How many cents can you save on each apple from buying $4 for 10 apples than from $3 for 6 apples?"""
    first_store_price = 3
    first_store_apples = 6
    second_store_price = 4
    second_store_apples = 10
    first_store_price_per_apple = first_store_price / first_store_apples
    second_store_price_per_apple = second_store_price / second_store_apples
    savings_per_apple = round((second_store_price_per_apple - first_store_price_per_apple) * 100)
    result = savings_per_apple
    return result

print(solution())