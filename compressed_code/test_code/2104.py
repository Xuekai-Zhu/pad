def solution():
    
    crate_capacity = 20
    num_crates = 3
    total_capacity = crate_capacity * num_crates
    buy_price = 330
    sell_price = 6
    rotten_tomatoes = 3
    total_good_tomatoes = total_capacity - rotten_tomatoes
    total_sales = total_good_tomatoes * sell_price
    profit = total_sales - buy_price
    result = profit
    return result

print(solution())