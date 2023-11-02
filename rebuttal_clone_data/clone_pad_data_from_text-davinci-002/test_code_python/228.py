def solution():
    """A company has 200 employees. 60% of the employees drive to work. Of the employees who don't drive to work, half take public transportation. How many more employees drive to work than take public transportation?"""
    total_employees = 200
    employees_driving = total_employees * 0.6
    employees_not_driving = total_employees - employees_driving
    employees_taking_public_transportation = employees_not_driving / 2
    employees_not_taking_public_transportation = employees_not_driving - employees_taking_public_transportation
    result = employees_not_taking_public_transportation - employees_taking_public_transportation
    
    return result

print(solution())