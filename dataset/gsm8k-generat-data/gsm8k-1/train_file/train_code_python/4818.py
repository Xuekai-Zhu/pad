def solution():
    """Nick is asking all his co-workers to chip in for a birthday gift for Sandra that costs $100. The boss agrees to contribute $15, and Todd volunteers to contribute twice as much since he always has to one-up everyone. If the remaining 5 employees (counting Nick) each pay an equal amount, how much do they each pay?"""
    total_cost = 100
    boss_contribution = 15
    todd_contribution = 2 * boss_contribution
    remaining_cost = total_cost - boss_contribution - todd_contribution
    num_employees = 5
    employee_contribution = remaining_cost / num_employees
    result = employee_contribution
    return result

print(solution())