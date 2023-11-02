def solution():
    """Sara got her first paycheck of two weeks of work. She had worked 40 hours a week at $11.50 per hour. The first thing she did was buy a new set of tires for her car for $410. How much money was she left with?"""
    hours_per_week = 40
    pay_rate = 11.50
    weeks_worked = 2
    gross_pay = hours_per_week * pay_rate * weeks_worked
    expenses = 410
    net_pay = gross_pay - expenses
    result = net_pay
    return result

print(solution())