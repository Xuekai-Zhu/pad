def solution():
    """Lanie has been sick and was only able to work 4/5 of her usual 40-hour week. If her hourly rate is $15, how much was her salary for that week?"""
    # Define Lanie's hourly rate and usual working hours
    hourly_rate = 15
    usual_hours = 40

    # Calculate Lanie's actual working hours for the week 
    actual_hours = usual_hours * (4/5)

    # Calculate Lanie's salary for the week based on her actual working hours
    salary = actual_hours * hourly_rate

    result = salary
    return result

print(solution())