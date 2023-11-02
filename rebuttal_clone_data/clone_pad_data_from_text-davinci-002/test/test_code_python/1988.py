def solution():
    total_employees = 100
    employees_driving = total_employees * (60 / 100)
    employees_not_driving = total_employees - employees_driving
    employees_taking_public_transportation = employees_not_driving / 2
    result = employees_taking_public_transportation
    return result

print(solution())