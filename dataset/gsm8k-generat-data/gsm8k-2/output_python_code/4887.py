def solution():
    """Patrick has been saving money to buy a bicycle that costs $150. He saved half the price but he then lent $50 to his friend. How much money does Patrick have now?"""
    bike_price = 150
    saved_amount = bike_price / 2
    lent_amount = 50
    remaining_amount = saved_amount - lent_amount
    result = remaining_amount
    return result

print(solution())