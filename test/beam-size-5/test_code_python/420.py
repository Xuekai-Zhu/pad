def solution():
    # Calculate the total capacity of the day trip
    total_capacity = 4 * 60

    # Calculate the number of employees that can be added to the minibusses
    added_employees = 6 * 30

    # Calculate the number of employees that can be added to the minivans
    added_employees = 10 * 15

    # Calculate the total number of employees that can be added to the day trip
    total_employees = added_employees + added_employees
    result = total_employees
    return result

print(solution())