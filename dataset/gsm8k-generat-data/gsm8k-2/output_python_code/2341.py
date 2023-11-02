def solution():
    """An internet provider gives a 5% discount if the customer pays before the 25th day of the month. If the monthly internet rate is $50, how much did the customer pay in all for 4 months if he paid every 25th of the month?"""
    monthly_rate = 50
    discount_rate = 0.05
    discount_amount = monthly_rate * discount_rate
    total_amount_per_month = monthly_rate - discount_amount
    total_amount_paid = total_amount_per_month * 4
    result = total_amount_paid
    return result

print(solution())