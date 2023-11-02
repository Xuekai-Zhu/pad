def solution():
    # Define the prices of the items
    bread_price = 2
    butter_price = 3
    juice_price = 2 * bread_price

    # Calculate the total cost of the items
    total_cost = bread_price + butter_price + juice_price

    # Calculate the amount of money Paul had left after his shopping
    money_left = 15 - total_cost
    result = money_left
    return result

print(solution())