def solution():
    """Nick is asking all his co-workers to chip in for a birthday gift for Sandra that costs $100. The boss agrees to contribute $15, and Todd volunteers to contribute twice as much since he always has to one-up everyone. If the remaining 5 employees (counting Nick) each pay an equal amount, how much do they each pay?"""
    # Define the total cost of the gift and the contributions of the boss and Todd
    total_cost = 100
    boss_contribution = 15
    todd_contribution = 2 * boss_contribution

    # Calculate the remaining amount needed from the 5 employees
    remaining_amount = total_cost - boss_contribution - todd_contribution

    # Calculate the amount each of the 5 employees needs to pay
    each_employee_contribution = remaining_amount / 5

    result = each_employee_contribution
    return result

print(solution())