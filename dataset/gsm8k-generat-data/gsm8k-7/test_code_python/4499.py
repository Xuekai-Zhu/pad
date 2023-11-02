def solution():
    current_job_hours = 8
    current_wage_per_hour = 10
    new_job_hours = 4
    new_wage_per_hour = 15
    bonus_per_week = 35

    # Calculate Maisy's earnings at her current job per week
    current_earnings = current_job_hours * current_wage_per_hour

    # Calculate Maisy's earnings at her new job per week
    new_earnings = (new_job_hours * new_wage_per_hour) + bonus_per_week

    # Calculate the difference between earnings at her current job and earnings at her new job
    difference = new_earnings - current_earnings
    result = difference
    return result

print(solution())