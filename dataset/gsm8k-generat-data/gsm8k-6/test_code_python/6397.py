def solution():
    # Calculate the weekly cost of the first employee
    cost_employee1 = 20 * 40  # hourly rate of $20, 40 hours per week

    # Calculate the weekly cost of the second employee
    cost_employee2 = (22-6) * 40  # hourly rate of $22 with a $6/hour subsidy, 40 hours per week

    # Calculate the amount of money per week Casey would save by hiring the cheaper employee
    savings_per_week = cost_employee1 - cost_employee2
    result = savings_per_week
    return result

print(solution())