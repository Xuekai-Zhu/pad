def solution():
    """An internet provider gives a 5% discount if the customer pays before the 25th day of the month. If the monthly internet rate is $50, how much did the customer pay in all for 4 months if he paid every 25th of the month?"""
    monthly_rate = 50
    discounted_rate = monthly_rate * 0.95
    payment_date = 25
    months = 4
    total_cost = (discounted_rate * payment_date * months) + (monthly_rate * (30-payment_date) * months)
    result = total_cost
    return result

print(solution())