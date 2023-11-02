def solution():
    # Define the number of hours worked by each employee
    fiona_hours = 40
    john_hours = 30
    jeremy_hours = 25

    # Calculate the total number of hours worked
    total_hours = fiona_hours + john_hours + jeremy_hours

    # Calculate the total cost of wages
    wage_cost = total_hours * 20

    result = wage_cost
    return result

print(solution())