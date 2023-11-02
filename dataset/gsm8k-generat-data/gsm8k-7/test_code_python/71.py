def solution():
    price_per_craft = 12
    num_crafts_sold = 3
    extra_money = 7
    deposit_amount = 18

    # Calculate the total amount of money Hillary made from selling crafts
    total_money_earned = (price_per_craft * num_crafts_sold) + extra_money

    # Calculate how much money Hillary is left with after depositing some of her profits
    money_left = total_money_earned - deposit_amount
    result = money_left
    return result

print(solution())