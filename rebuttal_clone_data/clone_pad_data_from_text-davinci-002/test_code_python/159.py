def solution():
    """At Mario's barbershop haircuts are 50% more expensive during the weekends. If Mario paid $18 for his last haircut on Monday, how much he would have paid the day before?"""
    price_paid = 18
    percent_increase = 50
    increase_amount = price_paid * (percent_increase / 100)
    weekend_price = price_paid + increase_amount
    result = weekend_price
    
    return result

print(solution())