def solution():
    """Mandy’s phone data plan charges $30 per month for data. Her first month, she got a promotional rate of one-third the normal price. However, in the fourth month she went over her data limit and was charged an extra fee of $15. How much did Mandy pay in the first 6 months for data?"""
    monthly_fee = 30
    first_month_fee = monthly_fee / 3
    fourth_month_fee = monthly_fee + 15
    total_fee = first_month_fee + monthly_fee + monthly_fee + fourth_month_fee + monthly_fee + monthly_fee
    result = total_fee
    return result

print(solution())