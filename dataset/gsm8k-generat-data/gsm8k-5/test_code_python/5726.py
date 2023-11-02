def solution():
    # Calculate the total ratio of the amount of money the three have
    total_ratio = 4 + 5 + 6
    
    # Calculate the amount of money each person has based on the ratio and total amount of money they have
    cara_money = 4/total_ratio * 75
    janet_money = 5/total_ratio * 75
    jerry_money = 6/total_ratio * 75
    
    # Calculate the total amount of money Cara and Janet have
    cara_janet_money = cara_money + janet_money
    
    # Calculate the buying price of the oranges based on the total money Cara and Janet have
    buying_price = cara_janet_money / 2
    
    # Calculate the selling price of the oranges after a 80% discount
    selling_price = buying_price * 0.8
    
    # Calculate the loss Cara and Janet will make if they sell the oranges at the discounted price
    total_loss = (buying_price - selling_price) * 2
    
    result = total_loss
    return result

print(solution())