def solution():
    total_apples = 405
    apples_used = 150
    apples_sold = total_apples - apples_used
    money_made = 408
    price_per_bag = money_made / apples_sold
    result = price_per_bag
    return result

print(solution())