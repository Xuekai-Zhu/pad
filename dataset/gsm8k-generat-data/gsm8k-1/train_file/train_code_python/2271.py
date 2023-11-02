def solution():
    """A company hires employees on a contract basis, depending on the availability of work. In a particular month, they hired 200 more employees on the first week than on the second week, and 150 fewer employees on the second week than on the third week. If the number of employees hired on the fourth week was twice the number hired in the third week, and the number of employees on the fourth week was 400, what's the average number of employees hired per week?"""
    
    fourth_week = 400
    third_week = fourth_week / 2
    second_week = third_week + 150
    first_week = second_week + 200
    
    total_employees = first_week + second_week + third_week + fourth_week
    weeks_worked = 4
    
    avg_employees_per_week = total_employees / weeks_worked
    
    return avg_employees_per_week

print(solution())