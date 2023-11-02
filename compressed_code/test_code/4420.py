def solution():
    
    total_money = 75
    cara_money = 4 / (4 + 5 + 6) * total_money
    janet_money = 5 / (4 + 5 + 6) * total_money
    combined_money = cara_money + janet_money
    buying_price = combined_money / 2
    selling_price = 0.8 * buying_price
    loss = (buying_price - selling_price) * 2
    result = loss
    return result

print(solution())