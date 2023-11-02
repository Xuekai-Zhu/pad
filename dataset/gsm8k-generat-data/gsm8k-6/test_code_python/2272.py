def solution():
    # Calculate the number of employees hired in the third week
    employees_third_week = 400 / 2  # the number of employees hired on the fourth week was twice the number hired in the third week
    # Calculate the number of employees hired in the second week
    employees_second_week = employees_third_week + 150  # 150 fewer employees on the second week than on the third week
    # Calculate the number of employees hired in the first week
    employees_first_week = employees_second_week + 200  # 200 more employees on the first week than on the second week
    # Calculate the total number of employees hired
    total_employees_hired = employees_first_week + employees_second_week + employees_third_week + 400
    # Calculate the average number of employees hired per week
    average_employees_hired = total_employees_hired / 4
    result = average_employees_hired
    return result

print(solution())