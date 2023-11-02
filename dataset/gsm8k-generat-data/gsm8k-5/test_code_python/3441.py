def solution():
    gecko_price = 100  # Brandon sold the geckos for $100
    pet_store_price = 3 * gecko_price + 5  # The pet store sells the geckos for 5 more than 3 times the price that Brandon sold them for
    pet_store_profit = pet_store_price - gecko_price  # The pet store's profit is the difference between the price they sell the geckos for and the price they bought them from Brandon for
    result = pet_store_profit
    return result

print(solution())