def solution():
    initial_stock = 200 / 2  # the initial stock is half the stock Eliza buys
    sold_stock = initial_stock * (3 / 4)
    remaining_stock = initial_stock - sold_stock

    # Eliza's mother buys 300 more rings and adds them to the remaining stock
    remaining_stock += 300

    # 3 days later, 150 rings are sold
    remaining_stock -= 150

    result = remaining_stock
    return result

print(solution())