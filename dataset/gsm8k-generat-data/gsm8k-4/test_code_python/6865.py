def solution():
    """Scott wants to buy a skateboard. To make money, Scott sold berry smoothies for $3 a cup and cakes for $2 each. He sold 40 cups of smoothies and 18 cakes. How much money did he make?"""
    # Define the prices and quantities of smoothies and cakes
    smoothie_price = 3
    cake_price = 2
    smoothie_qty = 40
    cake_qty = 18

    # Calculate the total money made from selling smoothies and cakes
    smoothie_money = smoothie_price * smoothie_qty
    cake_money = cake_price * cake_qty
    total_money = smoothie_money + cake_money

    # return the result
    result = total_money
    return result

print(solution())