def solution():
    """A car manufacturing company that produces 100 cars per month wants to increase its production to reach 1800 cars per year. How many cars should the company add to the monthly production rate to reach that target?"""
    current_production = 100 * 12
    target_production = 1800
    cars_to_add = (target_production - current_production) / 12
    result = cars_to_add
    return result

print(solution())