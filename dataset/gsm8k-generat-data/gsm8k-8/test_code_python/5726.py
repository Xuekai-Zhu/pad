def solution():
    # Define the ratio of the amount of money each person has
    cara_to_janet_to_jerry_ratio = "4:5:6"

    # Calculate the total amount of money
    total_money = 75

    # Split the total money into 15 equal parts (4+5+6=15)
    one_part = total_money / 15

    # Calculate the amount of money Cara and Janet have together
    cara_janet_money = 4 * one_part + 5 * one_part

    # Calculate the buying price of the oranges
    buying_price = cara_janet_money / 2

    # Calculate the selling price of the oranges
    selling_price = buying_price * 0.8

    # Calculate the loss Cara and Janet will make
    loss = buying_price - selling_price
    result = loss
    return result

print(solution())