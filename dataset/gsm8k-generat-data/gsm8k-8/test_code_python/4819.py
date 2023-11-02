def solution():
    # Define the total cost of the gift and the contributions of the boss and Todd
    total_cost = 100
    boss_contribution = 15
    todd_contribution = 2 * boss_contribution

    # Calculate the remaining amount that needs to be paid by the 5 employees
    remaining_amount = total_cost - boss_contribution - todd_contribution

    # Calculate the amount that each of the 5 employees need to pay
    num_employees = 5
    each_employee_pays = remaining_amount / num_employees

    result = each_employee_pays
    return result

print(solution())