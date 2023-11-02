def solution():
    """Robby, Jaylen and Miranda are employed at a Cheesecake factory, earning $10 per hour. They work 10 hours a day, five days a week. Robby saves 2/5 of his salary, Jaylene saves 3/5 of his salary, while Miranda saves half of her salary. What are the combined savings of the three employees after four weeks?"""
    # Define the hourly rate and the number of working hours per week
    hourly_rate = 10
    weekly_hours = 10 * 5

    # Calculate the weekly salary of each employee
    robby_salary = hourly_rate * weekly_hours
    jaylene_salary = hourly_rate * weekly_hours
    miranda_salary = hourly_rate * weekly_hours

    # Calculate the savings of each employee
    robby_savings = robby_salary * (2/5)
    jaylene_savings = jaylene_salary * (3/5)
    miranda_savings = miranda_salary * 0.5

    # Calculate the combined savings of the three employees after four weeks
    combined_savings = (robby_savings + jaylene_savings + miranda_savings) * 4

    # return the result
    result = combined_savings
    return result

print(solution())