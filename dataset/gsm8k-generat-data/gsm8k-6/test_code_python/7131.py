def solution():
    # Calculate the amount of money Donna made every day
    morning_job = 2 * 10  # Donna worked 2 hours every morning walking dogs for $10.00 an hour
    after_school_job = 2 * 12.5  # Donna worked at a card shop for 2 hours and made $12.50 an hour
    guaranteed_babysitting = 10 * 4  # Donna was guaranteed 4 hours every Saturday babysitting for $10.00 an hour
    weekend_babysitting = 0  # Donna's weekend babysitting pay is not given
    daily_salary = morning_job + after_school_job + guaranteed_babysitting + weekend_babysitting

    # Calculate the total amount of money Donna made over 7 days
    total_salary = daily_salary * 7
    result = total_salary
    return result

print(solution())