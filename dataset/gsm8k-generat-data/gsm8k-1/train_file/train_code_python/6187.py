def solution():
    """Dino does some online gig work for a living. He works 20 hours a month making $10 an hour. He works 30 hours a month making $20 an hour. He works 5 hours a month making $40 an hour. He pays $500 a month in expenses. How much money does Dino have left at the end of the month?"""
    hours_10 = 20
    hours_20 = 30
    hours_40 = 5
    pay_10 = 10
    pay_20 = 20
    pay_40 = 40
    expenses = 500
    income = (hours_10 * pay_10) + (hours_20 * pay_20) + (hours_40 * pay_40)
    profit = income - expenses
    result = profit
    return result

print(solution())