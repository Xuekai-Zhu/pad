def solution():
    """Sara got her first paycheck of two weeks of work. She had worked 40 hours a week at $11.50 per hour. The first thing she did was buy a new set of tires for her car for $410. How much money was she left with?"""
    hours_per_week = 40
    hourly_wage = 11.50
    total_hours = hours_per_week * 2
    gross_pay = total_hours * hourly_wage
    remaining_money = gross_pay - 410
    result = remaining_money
    return result

print(solution())