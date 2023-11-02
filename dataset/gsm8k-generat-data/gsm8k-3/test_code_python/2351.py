def solution():
    """Lanie has been sick and was only able to work 4/5 of her usual 40-hour week. If her hourly rate is $15, how much was her salary for that week?"""
    # Define Lanie's usual weekly work hours and hourly rate
    USUAL_HOURS = 40
    HOURLY_RATE = 15

    # Calculate Lanie's hours worked for the sick week
    sick_hours = USUAL_HOURS * 4/5

    # Calculate Lanie's salary for the sick week
    salary = sick_hours * HOURLY_RATE

    # Display Lanie's salary for the sick week
    result = salary
    return result

print(solution())