def solution():
    # Calculate the total number of shirts produced in a day
    total_shirts = 20 * 20  # 20 employees each make 20 shirts per day

    # Calculate the total revenue generated from selling the shirts
    total_revenue = total_shirts * 35

    # Calculate the total cost of paying the employees
    total_employee_cost = 20 * 12 * 8 + total_shirts * 5

    # Calculate the total expenses apart from employee costs
    total_other_expenses = 1000

    # Calculate the net profit
    net_profit = total_revenue - total_employee_cost - total_other_expenses

    result = net_profit
    return result

print(solution())