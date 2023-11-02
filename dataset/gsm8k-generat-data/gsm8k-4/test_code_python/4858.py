def solution():
    """When Erick went to the market to sell his fruits, he realized that the price of lemons had risen by $4 for each lemon. The price of grapes had also increased by half the price that the price of lemon increased by per grape. If he had planned to sell the lemons at $8 and the grapes at $7, and he had 80 lemons and 140 grapes in his basket, how much money did he collect from selling the fruits at the new prices?"""
    # Define the initial prices of lemons and grapes
    lemon_price = 8
    grape_price = 7

    # Define the number of lemons and grapes in the basket
    num_lemons = 80
    num_grapes = 140

    # Calculate the new prices of lemons and grapes
    new_lemon_price = lemon_price + 4
    new_grape_price = grape_price + (4/2)

    # Calculate the total amount collected from selling lemons and grapes at the new prices
    total_money = (num_lemons * new_lemon_price) + (num_grapes * new_grape_price)

    result = total_money
    return result

print(solution())