def solution():
    
    # Define the hourly rates and hours worked
    teach_rate = 20
    coach_rate = 30
    teach_hours = 35
    coach_hours = 15

    # Calculate the annual salary
    teach_salary = teach_rate * teach_hours * 50
    coach_salary = coach_rate * coach_hours * 50
    annual_salary = teach_salary + coach_salary

    # return the result
    result = annual_salary
    return result

print(solution())