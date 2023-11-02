def solution():
    # Calculate the total hours worked by all employees in a week
    total_hours = 40 + 30 + 25

    # Calculate the total cost of paying all employees in a week
    total_wages = total_hours * 20  # employees are paid $20 per hour

    # Calculate the total cost of paying all employees in a month
    total_cost = total_wages * 4  # assuming a month has four weeks

    result = total_cost
    return result

print(solution())