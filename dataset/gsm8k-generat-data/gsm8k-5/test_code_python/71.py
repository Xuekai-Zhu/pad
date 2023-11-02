def solution():
    craft_price = 12  # Hillary sells each handmade craft for $12
    num_crafts_sold = 3  # Hillary sold 3 crafts today
    extra_money_from_customer = 7  # Hillary received an extra $7 from a customer
    total_profit = (craft_price * num_crafts_sold) + extra_money_from_customer  # Calculate Hillary's total profit
    deposit = 18  # Hillary deposited $18 of her profits into her bank account
    left_over = total_profit - deposit  # Calculate how much money Hillary has left after depositing into her account
    result = left_over
    return result

print(solution())