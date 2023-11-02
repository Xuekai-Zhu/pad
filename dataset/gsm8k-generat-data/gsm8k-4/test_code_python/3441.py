def solution():
    """Brandon sold some geckos to a local pet shop. Brandon sold the geckos for 100$. The pet store sells them for 5 more than 3 times that. How much does the pet store profit?"""
    # Define the selling price of the geckos
    selling_price = 100

    # Calculate the pet store's selling price
    pet_store_price = 3 * selling_price + 5

    # Calculate the profit made by the pet store
    profit = pet_store_price - selling_price

    # return the result
    result = profit
    return result

print(solution())