def solution():
    """Jill likes to do small jobs online. She makes $10 a day for her first month working online, and double that per day in her second month. Her third month she makes the same amount per day as the previous month, but only works every other day. How much did she make over three months, assuming each month is 30 days long?"""
    first_month_pay = 10 * 30
    second_month_pay = (10 * 2) * 30
    third_month_pay = ((10 * 2) * 30) / 2
    total_pay = first_month_pay + second_month_pay + third_month_pay
    result = total_pay
    return result

print(solution())