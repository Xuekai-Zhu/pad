def solution():
    
    num_items = 2000
    retail_price = 50
    discount_percent = 80
    sell_percent = 90
    sale_price = retail_price * (100 - discount_percent) / 100
    revenue = num_items * sale_price * sell_percent / 100
    remaining_money = revenue - 15000
    result = remaining_money
    return result

print(solution())