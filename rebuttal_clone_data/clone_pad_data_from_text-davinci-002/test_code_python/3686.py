def solution():
    money_given = 30000
    percent_increase = 100
    increase_amount = money_given * (percent_increase / 100)
    sale_price = increase_amount + money_given
    money_after_sale = sale_price / 2
    money_received = money_after_sale - money_given
    result = money_received
    return result

print(solution())