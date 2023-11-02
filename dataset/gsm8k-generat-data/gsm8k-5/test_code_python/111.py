def solution():
    bread_price = 2  # Paul bought bread for $2
    butter_price = 3  # Paul bought butter for $3
    juice_price = 2 * bread_price  # Paul bought juice which costs two times the price of bread
    total_price = bread_price + butter_price + juice_price  # Paul's total bill
    money_left = 15 - total_price  # Calculate how much money Paul has left after the shopping
    result = money_left
    return result

print(solution())