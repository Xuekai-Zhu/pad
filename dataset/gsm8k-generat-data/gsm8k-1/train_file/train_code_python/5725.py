def solution():
    """The ratio of the amount of money Cara, Janet, and Jerry have is 4:5:6. If the total amount of money they have is $75, calculate the loss Cara and Janet will make if they combine their money to buy oranges and sell them at 80% of the buying price."""
    total_ratio = 4 + 5 + 6
    cara_share = 4 / total_ratio
    janet_share = 5 / total_ratio
    jerry_share = 6 / total_ratio
    total_money = 75
    cara_money = total_money * cara_share
    janet_money = total_money * janet_share
    combined_money = cara_money + janet_money
    buying_price = combined_money
    selling_price = buying_price * 0.8
    loss = buying_price - selling_price
    result = loss
    
    return result

print(solution())