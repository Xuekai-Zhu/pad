def solution():
    # Calculate the total cost of employing all the employees for one 8-hour long shift
    cost = (200 * 12 + 40 * 14 + (300 - 200 - 40) * 17) * 8  # cost per hour multiplied by number of employees and hours worked
    result = cost
    return result

print(solution())