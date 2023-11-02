def solution():
    days_worked = 300  # Andrew worked 300 days last year
    days_off_march = 5  # Andrew took 5 days off in March
    days_off_september = 2 * days_off_march  # Andrew took twice as many days off in September

    # Calculate the total vacation days Andrew has earned
    vacation_days_earned = days_worked // 10

    # Calculate the total vacation days Andrew has used
    vacation_days_used = days_off_march + days_off_september

    # Calculate the remaining vacation days Andrew can take
    remaining_vacation_days = vacation_days_earned - vacation_days_used
    result = remaining_vacation_days
    return result

print(solution())