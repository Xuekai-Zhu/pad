def solution():
    # Calculate the total hours worked by all employees
    total_hours = 6 * 25 * 8

    # Calculate the total wage cost for the warehouse workers
    warehouse_cost = 4 * 15 * total_hours

    # Calculate the total wage cost for the managers
    manager_cost = 2 * 20 * total_hours

    # Calculate the total wage cost for all employees
    total_cost = warehouse_cost + manager_cost

    # Calculate the FICA tax amount
    fica_tax = total_cost * 0.1

    # Add the FICA tax to the total cost to get the final amount owed by Janet
    final_cost = total_cost + fica_tax
    result = final_cost
    return result

print(solution())