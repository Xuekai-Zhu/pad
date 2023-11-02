def solution():
    """Patrick has been saving money to buy a bicycle that costs $150. He saved half the price but he then lent $50 to his friend. How much money does Patrick have now?"""
    bike_price = 150
    saved_money = bike_price / 2
    money_lent = 50
    money_left = saved_money - money_lent
    result = money_left
    return result

print(solution())