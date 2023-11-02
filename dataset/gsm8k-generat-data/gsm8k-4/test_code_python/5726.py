def solution():
    """The ratio of the amount of money Cara, Janet, and Jerry have is 4:5:6. If the total amount of money they have is $75, calculate the loss Cara and Janet will make if they combine their money to buy oranges and sell them at 80% of the buying price."""
    # Define the ratio of money
    cara_money_ratio = 4
    janet_money_ratio = 5
    jerry_money_ratio = 6

    # Calculate the total ratio
    total_ratio = cara_money_ratio + janet_money_ratio + jerry_money_ratio

    # Calculate the total amount of money
    total_money = 75

    # Calculate the amount of money each person has
    cara_money = (cara_money_ratio/total_ratio) * total_money
    janet_money = (janet_money_ratio/total_ratio) * total_money
    jerry_money = (jerry_money_ratio/total_ratio) * total_money

    # Calculate the total amount paid for the oranges
    total_paid = cara_money + janet_money

    # Calculate the selling price of the oranges at 80% of the buying price
    selling_price = total_paid * 0.8

    # Calculate the loss made by Cara and Janet
    loss = (total_paid - selling_price) / 2

    result = loss
    return result

print(solution())