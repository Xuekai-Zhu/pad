def solution():
    # Define the total operation costs
    total_costs = 4000

    # Calculate the amount spent on employees' salaries
    employee_salary_costs = (2/5) * total_costs

    # Calculate the remaining amount after paying for employee salaries
    remaining_costs = total_costs - employee_salary_costs

    # Calculate the amount spent on delivery costs
    delivery_costs = (1/4) * remaining_costs

    # Calculate the amount spent on orders done
    order_costs = remaining_costs - delivery_costs

    result = order_costs
    return result

print(solution())