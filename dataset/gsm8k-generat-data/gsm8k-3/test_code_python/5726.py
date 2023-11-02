def solution():
    """The ratio of the amount of money Cara, Janet, and Jerry have is 4:5:6. If the total amount of money they have is $75, calculate the loss Cara and Janet will make if they combine their money to buy oranges and sell them at 80% of the buying price."""
    # Define the ratio of the amount of money Cara, Janet, and Jerry have
    CARA_RATIO = 4
    JANET_RATIO = 5
    JERRY_RATIO = 6

    # Calculate the total amount of money
    total_money = 75

    # Calculate the amount of money Cara has
    cara_money = (CARA_RATIO / (CARA_RATIO + JANET_RATIO + JERRY_RATIO)) * total_money

    # Calculate the amount of money Janet has
    janet_money = (JANET_RATIO / (CARA_RATIO + JANET_RATIO + JERRY_RATIO)) * total_money

    # Calculate the total amount of money Cara and Janet have
    total_cara_janet_money = cara_money + janet_money

    # Calculate the buying price of the oranges
    buying_price = total_cara_janet_money / 2

    # Calculate the selling price of the oranges
    selling_price = buying_price * 0.8

    # Calculate the loss
    loss = (buying_price - selling_price) * 2

    # Display the loss
    result = loss
    return result

print(solution())