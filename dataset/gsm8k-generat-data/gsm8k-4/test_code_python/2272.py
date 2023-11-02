def solution():
    """A company hires employees on a contract basis, depending on the availability of work. In a particular month, they hired 200 more employees on the first week than on the second week, and 150 fewer employees on the second week than on the third week. If the number of employees hired on the fourth week was twice the number hired in the third week,  and the number of employees on the fourth week was 400, what's the average number of employees hired per week?"""
    # Calculate the number of employees hired in the third week
    employees_third_week = 400 / 2

    # Calculate the number of employees hired in the second week
    employees_second_week = employees_third_week + 150

    # Calculate the number of employees hired in the first week
    employees_first_week = employees_second_week + 200

    # Calculate the total number of employees hired in the month
    total_employees = employees_first_week + employees_second_week + employees_third_week + 400

    # Calculate the average number of employees hired per week
    average_employees = total_employees / 4

    result = round(average_employees)
    return result

print(solution())