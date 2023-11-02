def solution():
    tea_price = 10
    cheese_price = tea_price / 2
    butter_price = 0.8 * cheese_price
    bread_price = butter_price / 2

    # Calculate the total cost of all items
    total_cost = butter_price + bread_price + cheese_price + tea_price
    result = total_cost
    return result

print(solution())