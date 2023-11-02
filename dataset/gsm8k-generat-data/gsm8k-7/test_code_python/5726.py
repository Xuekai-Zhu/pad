def solution():
    total_ratio = 4 + 5 + 6  # total ratio of money
    total_money = 75  # total amount of money they have

    # Calculate the amount of money each person has
    cara_money = total_money * (4 / total_ratio)
    janet_money = total_money * (5 / total_ratio)
    jerry_money = total_money * (6 / total_ratio)

    # Calculate the total money Cara and Janet have
    cara_janet_money = cara_money + janet_money

    # Calculate the buying price of oranges
    buying_price = cara_janet_money / 2

    # Calculate the selling price of oranges at 80% of the buying price
    selling_price = buying_price * 0.8

    # Calculate the total loss Cara and Janet will make
    total_loss = (buying_price - selling_price) * 2
    result = total_loss
    return result

print(solution())