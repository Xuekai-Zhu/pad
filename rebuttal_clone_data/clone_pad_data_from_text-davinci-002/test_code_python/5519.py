def solution():
    brownies_brought = 30 * 12
    cookies_brought = 20 * 24
    donuts_brought = 15 * 12
    total_items = brownies_brought + cookies_brought + donuts_brought
    price_per_item = 2
    total_money_made = total_items * price_per_item
    result = total_money_made
    
    return result

print(solution())