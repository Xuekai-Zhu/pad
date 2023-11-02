def solution():
    # Calculate the total ratio of the amount of money they have
    total_ratio = 4 + 5 + 6

    # Calculate the amount of money Cara and Janet have
    cara_share = 4 / total_ratio * 75
    janet_share = 5 / total_ratio * 75

    # Calculate the buying price of the oranges
    buying_price = cara_share + janet_share

    # Calculate the selling price after getting an 80% discount
    selling_price = buying_price * 0.8

    # Calculate the profit/loss made by Cara and Janet
    profit_loss = selling_price - buying_price

    result = round(profit_loss, 2)
    return result

print(solution())