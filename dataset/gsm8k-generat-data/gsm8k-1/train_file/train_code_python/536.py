def solution():
    """A shipping boat's crew consisted of 17 sailors, with five inexperienced sailors. Each experienced sailor was paid 1/5 times more than the inexperienced sailors. If the inexperienced sailors were paid $10 per hour for a 60-hour workweek, calculate the total combined monthly earnings of the experienced sailors."""
    num_sailors = 17
    num_inexperienced = 5
    num_experienced = num_sailors - num_inexperienced
    hourly_wage_inexperienced = 10
    weekly_hours = 60
    monthly_hours = weekly_hours * 4
    inexperienced_salary = num_inexperienced * hourly_wage_inexperienced * weekly_hours
    experienced_salary = inexperienced_salary * 1.2 # 1/5 more is the same as multiplying by 1.2
    total_salary = experienced_salary * num_experienced
    result = total_salary
    return result

print(solution())