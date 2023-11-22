def solution():
    
    # Define the number of employees in each group
    employees_per_group = 200

    # Define the number of group assignments
    group_assignments = 7

    # Calculate the total number of employees
    total_employees = employees_per_group * 3

    # Calculate the total number of people on the tour
    total_people = total_employees * group_assignments

    # return the result
    result = total_people
    return result

print(solution())