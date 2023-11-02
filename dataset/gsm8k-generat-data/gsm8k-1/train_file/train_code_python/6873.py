def solution():
    """Mandy’s phone data plan charges $30 per month for data. Her first month, she got a promotional rate of one-third the normal price. However, in the fourth month she went over her data limit and was charged an extra fee of $15. How much did Mandy pay in the first 6 months for data?"""
    normal_price = 30
    promo_price = normal_price / 3
    months_paid = 6
    extra_fee = 15
    total_cost = (promo_price + (normal_price * (months_paid - 2)) + extra_fee)
    result = total_cost
    return result

print(solution())