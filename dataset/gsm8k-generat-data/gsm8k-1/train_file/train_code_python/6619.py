def solution():
    """Robby, Jaylen and Miranda are employed at a Cheesecake factory, earning $10 per hour. They work 10 hours a day, five days a week. Robby saves 2/5 of his salary, Jaylene saves 3/5 of his salary, while Miranda saves half of her salary. What are the combined savings of the three employees after four weeks?"""
    hourly_wage = 10
    hours_per_day = 10
    days_per_week = 5
    weeks = 4
    
    robbys_salary = hourly_wage * hours_per_day * days_per_week * weeks
    jaylens_salary = hourly_wage * hours_per_day * days_per_week * weeks
    mirandas_salary = hourly_wage * hours_per_day * days_per_week * weeks
    
    robbys_savings = robbys_salary * (2/5)
    jaylens_savings = jaylens_salary * (3/5)
    mirandas_savings = mirandas_salary * 0.5
    
    combined_savings = robbys_savings + jaylens_savings + mirandas_savings
    result = combined_savings
    return result

print(solution())