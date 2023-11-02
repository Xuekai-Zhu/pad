def solution():
    """Brandon sold some geckos to a local pet shop. Brandon sold the geckos for 100$. The pet store sells them for 5 more than 3 times that. How much does the pet store profit?"""
    brandon_sale_price = 100
    pet_store_sale_price = 3 * brandon_sale_price + 5
    profit = pet_store_sale_price - brandon_sale_price
    result = profit
    return result

print(solution())